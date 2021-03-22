from django.contrib import auth
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='cuentas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_user, name='edit_user'),
    path('<int:pk>/edit/', views.admin_edit_user, name='admin_edit_user'),
    path('<int:pk>/edit2/', views.admin_edit_user2, name='admin_edit_user2'),
    path('permission-error/', views.permission_error, name='perm_error'),
]
