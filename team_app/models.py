from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField

from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class TeamModel(models.Model):
    user = models.ForeignKey(User, related_name="team", on_delete=models.CASCADE, verbose_name=_("User"))
    skills = RichTextField(verbose_name=_("skills"))
    position = models.CharField(max_length=200, blank=True, verbose_name=_("position"))

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = _("team member")
        verbose_name_plural = _("Team members")


class ContactModel(models.Model):
    phone = models.CharField(max_length=12, verbose_name=_("phone"))
    fax = models.CharField(max_length=12, blank=True, verbose_name=_("fax"))
    address = models.TextField(verbose_name=_("address"))
    email = models.EmailField(verbose_name=_("E-mail"))

    def __str__(self):
        return "{0} {1} {2}".format(self.phone, self.fax, self.email)

    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")


class ServiceModel(models.Model):
    icon = models.CharField(max_length=50, verbose_name=_("icon style"))
    title = models.CharField(max_length=250, verbose_name=_("type of service"))
    desc = RichTextField(verbose_name=_("description"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("service list")


class AboutModel(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("title"))
    body = RichTextField(verbose_name=_('body'))

    class Meta:
        verbose_name = _("about")
        verbose_name_plural = _("abouts")


class CertificatesModel(models.Model):
    user = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name="cert", verbose_name=_("Team member"))
    image = ImageField(upload_to="team/certificates/", blank=True, verbose_name=_("Image"))

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = _("certificate")
        verbose_name_plural = _("certificate list")


class FeedbackModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(max_length=200, verbose_name=_("subject"))
    body = models.TextField(verbose_name=_("message body"))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("Created date"))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("feedback message")
        verbose_name_plural = _("feedbacks")
