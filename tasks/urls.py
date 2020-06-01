from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTask, name='add'),
    path('check/<id>', views.checked, name='check'),
    path('done', views.done, name='done'),
    path('active', views.active, name='active'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
    path('delete/<id>', views.deleteOne, name="deleteOne")
]