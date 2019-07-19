from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


class TeamModel(models.Model):
    user = models.ForeignKey(USER_MODEL, related_name="team", on_delete=models.CASCADE, verbose_name=_("User"))
    position = models.CharField(max_length=200, blank=True, verbose_name=_("position"))
    photo = models.ImageField(upload_to="team/", blank=True, verbose_name=_("photo"))

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = _("team member")
        verbose_name_plural = _("Team members")


class SkillModel(models.Model):
    user = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name="skill", verbose_name=_("team member"))
    skill = models.TextField(verbose_name=_("skill item"))

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skill list")


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("service list")


class ServiceItemModel(models.Model):
    title = models.ForeignKey(
        ServiceModel,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("service title")
    )
    desc = models.TextField(verbose_name=_("service item"))

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = _("service item")
        verbose_name_plural = _("service item list")


class AboutModel(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("title"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("about")
        verbose_name_plural = _("abouts")


class AboutItemModel(models.Model):
    title = models.ForeignKey(AboutModel, on_delete=models.CASCADE, related_name="items", verbose_name=_("about title"))
    desc = models.CharField(max_length=250, verbose_name=_("about item"))

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = _("about item")
        verbose_name_plural = _("about item list")


class CertificatesModel(models.Model):
    user = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name="cert", verbose_name=_("Team member"))
    image = models.ImageField(upload_to="team/certificates/", blank=True, verbose_name=_("Image"))

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
