from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_names, name='list'),
    path('add/', views.AddName.as_view(), name='add'),
]
