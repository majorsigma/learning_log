"""Defines a URL patterns for leaning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'              # Namespace name
urlpatterns = [
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
