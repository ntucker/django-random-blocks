from django import template
from django.db.models import Q
from django.utils.safestring import mark_safe

from utils.weighted_sampling import WalkerRandomSampling

from ..models import Block

register = template.Library()


@register.simple_tag
def random_blocks(request):
    blocks = list(Block.objects.select_related().filter(Q(site=request.account) | Q(site__isnull=True)))
    if blocks:
        sampler = WalkerRandomSampling([snip.weight for snip in blocks], blocks)
        return mark_safe(sampler.random().render())
    return ""
