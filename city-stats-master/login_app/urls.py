
from django.urls import path
from . import views
from login_app.graph_apps import app

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('homepage', views.homepage),
    path('saved_cities', views.saved_cities),
    path('save', views.save_new_city),
    path('mycitiesplot', views.my_cities_plot)
]