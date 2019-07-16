from django.views.generic import edit
from django.urls import reverse_lazy
from team_app.forms import FeedbackForm


class TeamView(edit.CreateView):
    template_name = 'team.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('team_app:index')
