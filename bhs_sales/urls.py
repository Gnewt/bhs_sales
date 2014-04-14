from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bhs_sales.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'shirts.views.product_list', name='home'),
    url(r'^orders/', 'shirts.views.orders', name='orders'),
    url(r'^info/', 'shirts.views.info', name='info'),
    url(r'^charge/', 'shirts.views.charge', name='charge'),
    url(r'^confirmation/(\d*)', 'shirts.views.confirmation', name='confirmation'),
)
