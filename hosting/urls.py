from django.urls import path
from . import views

urlpatterns = [
    path('receive-git-link/', views.receive_git_link, name='receive_git_link'),
]
