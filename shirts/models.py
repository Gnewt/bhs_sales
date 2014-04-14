from django.db import models
from json_field import JSONField

SMALL = 'S'
MEDIUM = 'M'
LARGE = 'L'
XLARGE = 'XL'

ITEM_SIZE_CHOICES = (
        (SMALL, 'Small (S)'),
        (MEDIUM, 'Medium (M)'),
        (LARGE, 'Large (L)'),
        (XLARGE, 'Extra Large (XL)'),
)

class StoreItem(models.Model):
    name = models.CharField(max_length=128)
    image = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    item = models.ForeignKey("shirts.StoreItem")
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    size = models.CharField(max_length=2,
                            choices=ITEM_SIZE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_charge_id = models.CharField(max_length=64, blank=True, null=True)
    notes = models.TextField(blank=True)

    STRIPE = 'ST'
    OTHER = 'OT'

    PAYMENT_METHOD_CHOICES = (
            (STRIPE, 'Stripe'),
            (OTHER, 'Other'),
    )

    payment_method = models.CharField(max_length=2,
                                      choices=PAYMENT_METHOD_CHOICES,
                                      default=STRIPE)

    def __unicode__(self):
        return "%s %s: %s (%s)" % (self.first_name, self.last_name, self.item.name, self.size)
