from django.urls import path
from team_app.views import TeamView


app_name = "team_app"

urlpatterns = [
    path('', TeamView.as_view(), name="index")
]
