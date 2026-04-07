from django.shortcuts import render,redirect
from hospitalapp.models import *
from webapp.models import RegistrationDb,ContactDb


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
    doctors=DoctorDb.objects.all()
    return render(request, 'Doctors.html',{'doctors':doctors})
def contact(request):
    return render(request, 'Contact.html')
def filtered_doctors(request,dep_name):
    doctors_filtered=DoctorDb.objects.filter(Department=dep_name)
    return render(request, 'Filtered_Doctors.html',{'doctors_filtered':doctors_filtered})
def single_doctor(request,d_id):
    single_doctor=DoctorDb.objects.get(id=d_id)
    return render(request, 'Single_Doctor.html',{'single_doctor':single_doctor})
def sign_in(request):
    return render(request, 'Sign_In.html')
def sign_up(request):
    return render(request, 'Sign_Up.html')
def booking(request,doctor_id):
    single_doctor=DoctorDb.objects.get(id=doctor_id)
    return render(request, 'Booking.html',{'single_doctor':single_doctor})
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            print("Passwords do not match")
            return redirect("sign_up")

        if RegistrationDb.objects.filter(name=name).exists():
            print("Username already exists")
            return redirect("sign_up")
        if RegistrationDb.objects.filter(email=email).exists():
            print("Email already exists")
            return redirect("sign_up")
        obj = RegistrationDb(
            name=name,
            email=email,
            password=password,
            confirm_password=confirm_password
        )
        obj.save()
        return redirect("sign_in")
def user_login(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        if RegistrationDb.objects.filter(name=uname,password=pswd).exists():
            request.session['username']=uname
            request.session['password']=pswd
            return redirect('home')
        else:
            return redirect('sign_in')
    else:
        return redirect('sign_in')
def save_contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        obj=ContactDb(Name=name,Email=email,Message=message)
        obj.save()
        return redirect(contact)
