from django.db import models

import jsonfield


class Block(models.Model):
    context = jsonfield.JSONField()
    weight = models.IntegerField(default=1)
    template = models.ForeignKey('BlockTemplate')

    def render(self):
        return self.template.markup.format(**self.context)


class BlockTemplate(models.Model):
    name = models.CharField(max_length=70)
    markup = models.TextField()

    def __unicode__(self):
        return self.name
