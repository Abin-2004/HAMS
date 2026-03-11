from django.shortcuts import render
from hospitalapp.models import *
from webapp.models import *


from hospitalapp.models import DoctorDb


# Create your views here.
def home(request):
    return render(request, 'Home.html')
def about(request):
    return render(request, 'About.html')
def all_departments(request):
    departments=DepartmentDb.objects.all()
    return render(request, 'All_Departments.html',{'departments':departments})
def doctors(request):
    return render(request, 'Doctors.html')
def contact(request):
    return render(request, 'Contact.html')
