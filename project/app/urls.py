from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='list', view=views.list_view, name='list'),
    path(route='register', view=views.register, name='register'),

]