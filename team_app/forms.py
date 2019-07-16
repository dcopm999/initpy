from django import forms
from django.utils.translation import ugettext_lazy as _

from team_app.models import FeedbackModel


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('NAME')}),
            'email': forms.TextInput(attrs={'placeholder': _('EMAIL')}),
            'subject': forms.TextInput(attrs={'placeholder': _('SUBJECT')}),
            'body': forms.Textarea(attrs={'placeholder': _('MESSAGE')}),
        }
