#from django.contrib import admin
from django.urls import path, include
from apps.todo.views import home_page

urlpatterns = [
    path('tasks/', include('apps.todo.urls')),
    path('', home_page)
]