from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('requisition', views.req_table, name='req_table'),
    path('add', views.req_Add,name='req_add'),
    path('success', views.success, name='success')
]
