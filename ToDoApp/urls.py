from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_task, name='add'),
    path('list/', views.list_task, name='list'),
    path('edit/<int:task_id>', views.edit_task, name='edit'),
]
