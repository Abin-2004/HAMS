from django.urls import path
from hospitalapp import views

urlpatterns = [
     path('dashboard/',views.dashboard,name='dashboard'),


    #Department
    path('add_department/',views.add_department,name='add_department'),
    path('display_department/',views.display_department,name='display_department'),
    path('save_department/',views.save_department,name='save_department'),
    path('delete_department/<int:department_id>/',views.delete_department,name='delete_department'),
    path('edit_department/<int:department_id>/',views.edit_department,name='edit_department'),
    path('update_department/<int:department_id>/',views.update_department,name='update_department'),


    #Doctors
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('display_doctor/',views.display_doctor,name='display_doctor'),
    path('save_doctor/',views.save_doctor,name='save_doctor'),
    path('delete_doctor/<int:doctor_id>/',views.delete_doctor,name='delete_doctor'),
    path('edit_doctor/<int:doctor_id>/',views.edit_doctor,name='edit_doctor'),
    path('update_doctor/<int:doctor_id>/',views.update_doctor,name='update_doctor'),

    #AAdmin
    path('admin_login_page/',views.admin_login_page,name='admin_login_page'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
]