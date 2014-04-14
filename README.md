BHS Shirt Sales
===============

Intro
-----

The BHS Class of 2014 needs some money for prom. We came up with the idea of selling senior shirts as a fundraiser, but the process for organizing an order for ~300 people is incredibly complex and comes with the headaches of having to lend money to make an order, collecting money afterward, over-ordering, etc.

This is our solution: a Stripe-based marketplace to preorder shirts. This lets us record the name/size/selection of everyone who wants a shirt, and then aggregate that data later. Payments are processed through Stripe.

Technical Stuff
---------------
This is a Django project. It currently only has one application, "shirts." Data is stored by default in SQLite, but that can be changed easily. Database migrations are handled through South.

I have included some deployment scripts, namely:  
  * `Makefile`
    *  Provides automated deployment, but will require changing of paths
  * `hup_bhssales`
    *  Used in my git post-receive hook to restart the server process automatically when I push new changes to production
  * `bin/gunicorn_start`
    * The script called by supervisord to start gunicorn -- will also require changing of paths for custom deployment

Supervisor keeps a gunicorn instance running with a socket in /tmp. I have set up nginx to proxy_pass to that socket, more or less just like any other Django project.

Architecture
------------

There are only two models.
1. StoreItem
    * Contains a name/description/summary/price of a certain item
2. Order
   * Contains the name of the customer, a timestamp, the purchase price (in case the price in the future changes), and the Stripe ID of the charge. The Stripe ID is optional -- I've allowed a separate "in person" payment type.

When the order form is submitted, `/charge` will use the Stripe Checkout token to attempt to make the charge through Stripe. If it's successful, an Order instance will be saved and the user redirected to a confirmation page. A public list of all orders is included.

The sizes are stored as a constant in `shirts/models.py`. I'm not sure this is the best way to do it.


Configuration
-------------

I have included my Dev configuration. I manage configurations using [django-configurations](http://django-configurations.readthedocs.org/en/latest/). You'll notice the end of `settings.py` tries to import all from `local_settings.py`. You'll need to create a `local_settings.py` in the same format as `settings.py`, containing a:

    class Production(Configuration):

Put your live Stripe keys in that configuration, without committing it to Git.

Also, run this in a venv. A `requirements.txt` is included.

