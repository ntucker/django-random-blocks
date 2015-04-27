from django.db import models
from django.utils.encoding import python_2_unicode_compatible, force_text

import jsonfield

from logos.pro_site.models import ProAccount


@python_2_unicode_compatible
class Block(models.Model):
    context = jsonfield.JSONField()
    weight = models.IntegerField(default=1)
    template = models.ForeignKey('BlockTemplate')
    site = models.ForeignKey(ProAccount, to_field="subdomain", blank=True, null=True)

    def render(self):
        print(self.context)
        return self.template.markup.format(**self.context)
    
    def __str__(self):
        return force_text(self.context)


@python_2_unicode_compatible
class BlockTemplate(models.Model):
    name = models.CharField(max_length=70)
    markup = models.TextField()
    site = models.ForeignKey(ProAccount, to_field="subdomain", blank=True, null=True)

    def __str__(self):
        return self.name
