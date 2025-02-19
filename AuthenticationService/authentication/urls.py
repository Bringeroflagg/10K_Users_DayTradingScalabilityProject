from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/auth/register/', views.register, name='register'),
    path('api/v1/auth/login/', views.login, name='login'),
    path('api/v1/auth/delete/<str:user_name>/', views.delete, name='delete'),
]
