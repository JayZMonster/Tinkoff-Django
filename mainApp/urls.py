from django.urls import path
from . import views

urlpatterns = [
  path("", views.MainPage.as_view(), name='main'),
  path("settings/", views.Settings.as_view(), name='settings'),
  path("terminal/", views.Terminal.as_view(), name='terminal')
]