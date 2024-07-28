from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontPage, name='frontPage'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('forgotPass/', views.forgotPass, name='forgotPass'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/frontPage.html'), name='logout'),
]