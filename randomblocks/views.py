from django.http import HttpResponse

from .models import Block
from .templatetags.random_block import random_blocks


def random_block(request):
    return HttpResponse(random_blocks(request))
