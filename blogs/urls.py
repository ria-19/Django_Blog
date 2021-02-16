"""Defining URP patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    #Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    #Details page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding a new blog.
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page for editing existing blogs.
    path('edit_entry/<int:topic_id>/', views.edit_entry, name='edit_entry'),
]