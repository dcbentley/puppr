from django.urls import path
from . import views
from rest_framework import DefaultRouter

urlpatterns = [
    path('', UserListView.as_view()),
    path('<pk>', UserDetailView.as_view()),
]
