from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), # GET and POST req. for insert operation
    path('<int:id>', views.employee_form, name="employee_update"), # GET and POST req. for update operation
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list') # GET req. to retrieve and display all records.
]
