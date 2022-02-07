from django.urls import path, include
from . import views

urlpatterns = [
    # get and post req. operations
    path('', views.employee_form, name='employee_insert'),
    # get and post req. for update
    path('<int:id>', views.employee_form, name='employee_update'),
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
    # get req. to retrieve and show
    path('list/', views.employee_list, name='employee_list'),
]
