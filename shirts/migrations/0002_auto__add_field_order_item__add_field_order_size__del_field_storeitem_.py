# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.item'
        db.add_column(u'shirts_order', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['shirts.StoreItem']),
                      keep_default=False)

        # Adding field 'Order.size'
        db.add_column(u'shirts_order', 'size',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=2),
                      keep_default=False)

        # Deleting field 'StoreItem.sizes'
        db.delete_column(u'shirts_storeitem', 'sizes')


    def backwards(self, orm):
        # Deleting field 'Order.item'
        db.delete_column(u'shirts_order', 'item_id')

        # Deleting field 'Order.size'
        db.delete_column(u'shirts_order', 'size')

        # Adding field 'StoreItem.sizes'
        db.add_column(u'shirts_storeitem', 'sizes',
                      self.gf('json_field.fields.JSONField')(default="{'Small (S)', 'Medium (M)', 'Large (L)', 'Extra Large (XL)'}"),
                      keep_default=False)


    models = {
        u'shirts.order': {
            'Meta': {'object_name': 'Order'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shirts.StoreItem']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'payment_method': ('django.db.models.fields.CharField', [], {'default': "'ST'", 'max_length': '2'}),
            'purchase_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'stripe_charge_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'shirts.storeitem': {
            'Meta': {'object_name': 'StoreItem'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['shirts']