from django.db import models
from django.utils.encoding import python_2_unicode_compatible, force_text

import jsonfield


@python_2_unicode_compatible
class Block(models.Model):
    context = jsonfield.JSONField()
    weight = models.IntegerField(default=1)
    template = models.ForeignKey('BlockTemplate')

    def render(self):
        return self.template.markup.format(**self.context)
    
    def __str__(self):
        return force_text(self.context)


@python_2_unicode_compatible
class BlockTemplate(models.Model):
    name = models.CharField(max_length=70)
    markup = models.TextField()

    def __str__(self):
        return self.name
