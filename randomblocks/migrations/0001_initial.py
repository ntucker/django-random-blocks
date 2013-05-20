# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Block'
        db.create_table(u'randomblocks_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('context', self.gf('jsonfield.fields.JSONField')(default={})),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['randomblocks.BlockTemplate'])),
        ))
        db.send_create_signal(u'randomblocks', ['Block'])

        # Adding model 'BlockTemplate'
        db.create_table(u'randomblocks_blocktemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('markup', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'randomblocks', ['BlockTemplate'])


    def backwards(self, orm):
        # Deleting model 'Block'
        db.delete_table(u'randomblocks_block')

        # Deleting model 'BlockTemplate'
        db.delete_table(u'randomblocks_blocktemplate')


    models = {
        u'randomblocks.block': {
            'Meta': {'object_name': 'Block'},
            'context': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['randomblocks.BlockTemplate']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'randomblocks.blocktemplate': {
            'Meta': {'object_name': 'BlockTemplate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markup': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['randomblocks']