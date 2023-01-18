from django.urls import path
from django.contrib.admin import views as auth_view
from . import views

urlpatterns = [
    path('', views.landing , name='landing'),

    #User Authentication
    path('login/', views.login_user, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout_user, name='logout')
]