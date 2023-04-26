from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_video/', views.add_video, name='add_video'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
]
