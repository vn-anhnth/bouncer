from django.urls import path

from . import views

app_name = 'bouncer'

urlpatterns = [
    path('', views.landing, name='landing'),
]
