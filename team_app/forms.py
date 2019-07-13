from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext_lazy as _

from team_app.models import TeamModel, FeedbackModel


class TeamForm(forms.ModelForm):
    skills = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = TeamModel
        fields = '__all__'


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
