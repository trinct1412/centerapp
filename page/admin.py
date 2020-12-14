from django.contrib import admin
from page.models import Page,Feed


class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(Feed, PageAdmin)
