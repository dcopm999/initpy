from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from team_app.models import (
    TeamModel,
    ContactModel,
    ServiceModel,
    AboutModel,
    CertificatesModel,
    FeedbackModel,
)
from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.


@admin.register(FeedbackModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created']


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']


class CertificatesAdmin(AdminImageMixin, admin.StackedInline):
    model = CertificatesModel


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    inlines = [
        CertificatesAdmin,
    ]
    list_display = ['user', 'position']
    autocomplete_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': (('user', 'position'),)
        }),
        (_('Skills'), {
            'fields': ('skills',)
        }),
    )


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone', 'fax', 'address', 'email']
    fieldsets = (
        (_('Contacts'), {
            'fields': (('phone', 'email'), 'fax')
        }),
        (_('Address'), {
            'fields': ('address',)
        })
    )


@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']
