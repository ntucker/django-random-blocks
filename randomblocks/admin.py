from django.contrib import admin

from .models import Block, BlockTemplate


class BlockAdmin(admin.ModelAdmin):
    list_display = ('context', 'weight', 'template', )


class BlockTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'markup', )

admin.site.register(Block, BlockAdmin)
admin.site.register(BlockTemplate, BlockTemplateAdmin)
