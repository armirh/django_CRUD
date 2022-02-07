from django.shortcuts import render

# Create your views here.

# function to retrieve and display employee record


def employee_list(request):
    return render(request, "employee_register/employee_list.html")


def employee_form(request):
    return render(request, "employee_register/employee_form.html")


def employee_delete(request):
    return
