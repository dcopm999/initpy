from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from team_app.models import (
    TeamModel,
    SkillModel,
    ContactModel,
    ServiceModel,
    ServiceItemModel,
    AboutModel,
    AboutItemModel,
    CertificatesModel,
    FeedbackModel,
)
# Register your models here.


@admin.register(FeedbackModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created']


class AboutItemAdmin(admin.StackedInline):
    model = AboutItemModel


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        AboutItemAdmin
    ]
    list_display = ['title']


class CertificatesAdmin(admin.StackedInline):
    model = CertificatesModel


class SkillItemAdmin(admin.StackedInline):
    model = SkillModel


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    inlines = [
        SkillItemAdmin,
        CertificatesAdmin,
    ]
    list_display = ['user', 'position']
    autocomplete_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': (('user', 'position'), 'photo')
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


class ServiceItemAdmin(admin.StackedInline):
    model = ServiceItemModel


@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    inlines = [
        ServiceItemAdmin
    ]
