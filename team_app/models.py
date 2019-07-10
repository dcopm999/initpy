from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class TeamModel(models.Model):
    user = models.ForeignKey(User, related_name="team", on_delete=models.CASCADE)
    skills = RichTextField(verbose_name=_("skills"))

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = _("team account")
        verbose_name_plural = _("Team accounts")
