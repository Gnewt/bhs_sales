import json
import stripe

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Sum
from django.conf import settings
from django.core.urlresolvers import reverse
from shirts.models import StoreItem, Order, ITEM_SIZE_CHOICES

# Create your views here.

def product_list(request):
    items = StoreItem.objects.all()
    return render_to_response("products.html", 
                              {'items': items,
                               'sizes': ITEM_SIZE_CHOICES},
                               context_instance = RequestContext(request))

def orders(request):
    total_collected = Order.objects.aggregate(Sum('purchase_price'))['purchase_price__sum']
    orders_total = Order.objects.count()
    orders = Order.objects.all().order_by('last_name')
    
    return render_to_response("orders.html",
                              {'total_collected': total_collected,
                               'orders_total': orders_total,
                               'orders': orders,
                              })

def info(request):
    return render_to_response("about.html")

def charge(request):
    if ('first_name' not in request.POST or
        'last_name' not in request.POST or
        'token' not in request.POST or
        'size' not in request.POST or
        'item' not in request.POST):
        return HttpResponseBadRequest("I didn't get enough data to complete your request. Contact Nick Mooney (nick@nickmooney.me).")
    
    item = StoreItem.objects.get(id=request.POST['item'])
    
    try:
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        charge = stripe.Charge.create(
            amount = int(item.price) * 100,
            currency = "usd",
            card = request.POST['token'],
            description = item.name,
            )

        order = Order()
        order.item = StoreItem.objects.get(id=int(request.POST['item']))
        order.first_name = request.POST['first_name']
        order.last_name = request.POST['last_name']
        order.size = request.POST['size']
        order.purchase_price = item.price
        order.stripe_charge_id = charge['id']

        order.save()
        
        return HttpResponseRedirect(reverse('confirmation', args=(order.id,)))

    except stripe.CardError, e:
        return HttpResponse("Your card was declined.")

def confirmation(request, id):
    order = Order.objects.get(id=id)
    size = ""
    for choice in ITEM_SIZE_CHOICES:
        if choice[0] == order.size:
            size = choice[1]
    return render_to_response("confirmation.html",
                              {'order': order,
                               'size': size,})
    