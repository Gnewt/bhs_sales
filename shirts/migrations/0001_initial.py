# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoreItem'
        db.create_table(u'shirts_storeitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('sizes', self.gf('json_field.fields.JSONField')(default="{'Small (S)', 'Medium (M)', 'Large (L)', 'Extra Large (XL)'}")),
        ))
        db.send_create_signal(u'shirts', ['StoreItem'])

        # Adding model 'Order'
        db.create_table(u'shirts_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('purchase_price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('stripe_charge_id', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('payment_method', self.gf('django.db.models.fields.CharField')(default='ST', max_length=2)),
        ))
        db.send_create_signal(u'shirts', ['Order'])


    def backwards(self, orm):
        # Deleting model 'StoreItem'
        db.delete_table(u'shirts_storeitem')

        # Deleting model 'Order'
        db.delete_table(u'shirts_order')


    models = {
        u'shirts.order': {
            'Meta': {'object_name': 'Order'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'payment_method': ('django.db.models.fields.CharField', [], {'default': "'ST'", 'max_length': '2'}),
            'purchase_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'stripe_charge_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'shirts.storeitem': {
            'Meta': {'object_name': 'StoreItem'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'sizes': ('json_field.fields.JSONField', [], {'default': '"{\'Small (S)\', \'Medium (M)\', \'Large (L)\', \'Extra Large (XL)\'}"'})
        }
    }

    complete_apps = ['shirts']