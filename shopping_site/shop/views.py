from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from .models import *
from django.db.models import Q


from django.http import HttpResponse
from .models import Hospital


# static data

def create_hospital_record(request):
    # Create a new hospital record
    new_record = Hospital.objects.create(
        fname="John",
        lname="Doe",
        age=30,
        salary=50000.00
    )
    return HttpResponse(f"Created Hospital Record: {new_record.fname} {new_record.lname}, Age: {new_record.age}, Salary: {new_record.salary}")

# create dynamic data



# def add_data(request):
#     if request.method == "POST":
#         fname = request.POST.get('fname', None)
#         lname = request.POST.get('lname', None)
#         age = request.POST.get('age', None)
#         salary = request.POST.get('salary', None)

#         if fname and lname and age and salary:
#             data = Hospital.objects.create(fname=fname, lname=lname, age=age, salary=salary)
#             data.save()
#             return HttpResponse(f"Data added successfully: {fname} {lname}, Age: {age}, Salary: {salary}")
#         else:
#             return HttpResponse("Error: All fields are required.")

#     return HttpResponse("Please submit the form with all required fields.")


print("Hello world")