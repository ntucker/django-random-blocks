from django.contrib import admin

from .models import Block, BlockTemplate


class BlockAdmin(admin.ModelAdmin):
    list_display = ('context', 'weight', 'template', 'site', )
    list_filter = ('site', )


class BlockTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'markup', 'site', )
    list_filter = ('site', )

admin.site.register(Block, BlockAdmin)
admin.site.register(BlockTemplate, BlockTemplateAdmin)
