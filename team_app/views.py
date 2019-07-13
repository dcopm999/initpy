from django.views.generic import edit
from django.urls import reverse_lazy
from team_app.forms import FeedbackForm
# Create your views here.


class HomeView(edit.CreateView):
    template_name = 'pages/home.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('home')
