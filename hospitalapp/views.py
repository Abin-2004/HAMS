from django.shortcuts import render
from django.shortcuts import render, redirect
from hospitalapp.models import DepartmentDb,DoctorDb

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



#Patient

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
    return render(request,'Edit_Doctor.html',{'data':data})


