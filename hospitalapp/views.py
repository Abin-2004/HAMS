from django.shortcuts import render
from django.shortcuts import render, redirect
from hospitalapp.models import DepartmentDb,DoctorDb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def dashboard(request):
    return render(request,'dashboard.html')

#Department
def add_department(request):
    return render(request,'Add_Department.html')
def display_department(request):
    department = DepartmentDb.objects.all()
    return render(request,'View_Department.html',{'department':department})
def save_department(request):
    if request.method == "POST":
        Department_Name = request.POST.get('Department_Name')
        Department_Description = request.POST.get('Department_Description')
        Department_Image = request.FILES.get('Department_Image')
        obj = DepartmentDb(
            Department_Name=Department_Name,
            Department_Description=Department_Description,
            Department_Image=Department_Image
        )
        obj.save()
        return redirect('add_department')
def delete_department(request,department_id):
    department = DepartmentDb.objects.filter(id=department_id)
    department.delete()
    return redirect('display_department')
def edit_department(request,department_id):
    department = DepartmentDb.objects.all()
    data=DepartmentDb.objects.get(id=department_id)
    return render(request,'Edit_Department.html',{'data':data,'department':department})
def update_department(request, department_id):
    if request.method == "POST":
        Department_Name = request.POST.get('Department_Name')
        Department_Description = request.POST.get('Department_Description')
        Department_Image = request.FILES.get('Department_Image')

        department = DepartmentDb.objects.get(id=department_id)

        department.Department_Name = Department_Name
        department.Department_Description = Department_Description

        if Department_Image:
            department.Department_Image = Department_Image
        department.save()
        return redirect('display_department')



#doctor

def add_doctor(request):
    department =DepartmentDb.objects.all()
    return render(request,'Add_Doctor.html',{'department':department})
def display_doctor(request):
    doctor = DoctorDb.objects.all()
    return render(request,'View_Doctor.html',{'doctor':doctor})
def save_doctor(request):
    if request.method == "POST":
        Doctor_Name = request.POST.get('Doctor_Name')
        Department= request.POST.get('Department')
        Email= request.POST.get('Email')
        Phone= request.POST.get('Phone')
        Qualification= request.POST.get('Qualification')
        Experience= request.POST.get('Experience')
        Image= request.FILES.get('Image')
        obj = DoctorDb(Doctor_Name=Doctor_Name,Department=Department,Email=Email,Phone=Phone,Qualification=Qualification,Experience=Experience,Image=Image)
        obj.save()
        return redirect('add_doctor')
def delete_doctor(request,doctor_id):
    doctor = DoctorDb.objects.filter(id=doctor_id)
    doctor.delete()
    return redirect('display_doctor')
def edit_doctor(request,doctor_id):
    data = DoctorDb.objects.get(id=doctor_id)
    department = DepartmentDb.objects.all()
    return render(request,'Edit_Doctor.html',{'data':data,'department':department})
def update_doctor(request, doctor_id):
    if request.method == "POST":
        Doctor_Name = request.POST.get('Doctor_Name')
        Department = request.POST.get('Department')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        Qualification = request.POST.get('Qualification')
        Experience = request.POST.get('Experience')
        Image = request.FILES.get('Image')

        doctor = DoctorDb.objects.get(id=doctor_id)

        doctor.Doctor_Name = Doctor_Name
        doctor.Department = Department
        doctor.Email = Email
        doctor.Phone = Phone
        doctor.Qualification = Qualification
        doctor.Experience = Experience
        if Image:
            doctor.Image = Image
        doctor.save()
        return redirect('display_doctor')


#Admin
def admin_login_page(request):
    return render(request,'Admin_Login.html')
def admin_login(request):
    if request.method =="POST":
        uname=request.POST.get('username')
        pswd=request.POST.get('password')

        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pswd

                return redirect(dashboard)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)
