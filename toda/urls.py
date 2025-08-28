from django.urls import path
from . import views
urlpatterns = [
    path("addTask/", views.addtask, name = "addtask"),
    path("markasdone/<int:pk>",views.markasdone ,name="markasdone"),
    path("markasundone/<int:pk>",views.markasundone ,name = "markasundone"),
    path("edit_task/<int:pk>",views.edit_task ,name="edit_task"),
    path("delete/<int:pk>",views.delete,name = "delete"),
]