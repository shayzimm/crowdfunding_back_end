from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUSerDetail.as_view()),
]