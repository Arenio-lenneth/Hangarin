"""
URL configuration for hangarin_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hangarin_project.hangarinorg.views import (
    HomePageView, TaskList, SubtaskList, CategoryList, PriorityList, NoteList, 
    TaskCreateView, SubtaskCreateView, CategoryCreateView, PriorityCreateView, NoteCreateView, 
    TaskUpdateView, SubtaskUpdateView, CategoryUpdateView, PriorityUpdateView, NoteUpdateView, 
    TaskDeleteView, SubtaskDeleteView, CategoryDeleteView, PriorityDeleteView, NoteDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("accounts/", include("allauth.urls")), # allauth routes

    #ListView
    path('task_list', TaskList.as_view(), name='task-list'),
    path('subtask_list', SubtaskList.as_view(), name='subtask-list'),
    path('category_list', CategoryList.as_view(), name='category-list'),
    path('priority_list', PriorityList.as_view(), name='priority-list'),
    path('note_list', NoteList.as_view(), name='note-list'),

    #CreateView
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('subtask_list/add', SubtaskCreateView.as_view(), name='subtask-add'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('priority_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('note_list/add', NoteCreateView.as_view(), name='note-add'),

    #UpdateView
    path('task_list/<pk>',TaskUpdateView.as_view(), name='task-update'),
    path('subtask_list/<pk>',SubtaskUpdateView.as_view(), name='subtask-update'),
    path('category_list/<pk>',CategoryUpdateView.as_view(), name='category-update'),
    path('priority_list/<pk>',PriorityUpdateView.as_view(), name='priority-update'),
    path('note_list/<pk>',NoteUpdateView.as_view(), name='note-update'),

    #DeleteView
    path('task_list/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('subtask_list/<int:pk>/delete', SubtaskDeleteView.as_view(), name='subtask-delete'),
    path('category_list/<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    path('priority_list/<int:pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),
    path('note_list/<int:pk>/delete', NoteDeleteView.as_view(), name='note-delete'),

]



