from django import template
from django.utils.safestring import mark_safe

from utils.weighted_sampling import WalkerRandomSampling

from ..models import Block

register = template.Library()


@register.simple_tag
def random_blocks():
    blocks = list(Block.objects.select_related().all())
    if blocks:
        sampler = WalkerRandomSampling([snip.weight for snip in blocks], blocks)
        return mark_safe(sampler.random().render())
    return ""
