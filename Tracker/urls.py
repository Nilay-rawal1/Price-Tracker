from django.urls import path
from django.contrib.admin import views as auth_view
from . import views

urlpatterns = [
    path('', views.landing),
    # path('login/', views.login, name = 'login'),

]