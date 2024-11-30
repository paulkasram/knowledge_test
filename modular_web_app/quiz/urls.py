from django.urls import path
from . import views

urlpatterns = [
    path('<str:topic_name>/', views.start_quiz, name='start_quiz'),
]
