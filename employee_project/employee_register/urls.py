from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form),  # localhost:p/employee/list
    path('list/', views.employee_list),
]
