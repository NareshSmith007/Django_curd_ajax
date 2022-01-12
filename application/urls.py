from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add_employee',views.add_employee),
    path('insert_employee',views.insert_employee),
    path('edit_employee/<int:myid>',views.edit_employee),
    path('update_employee',views.update_employee),
    path('delete_employee',views.delete_employee)
]