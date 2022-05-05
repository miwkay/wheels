from django.contrib import admin

from .models import Contact, Disc, Rubber

admin.site.register(Rubber)
admin.site.register(Disc)
admin.site.register(Contact)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
