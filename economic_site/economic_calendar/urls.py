from django.urls import path

from . import views

app_name = 'economic_calendar'
urlpatterns = [
    path('', views.index, name='index')
]