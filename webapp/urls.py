from django.urls import path
from webapp import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('all_departments/',views.all_departments, name='all_departments'),
    path('doctors/',views.doctors, name='doctors'),
    path('contact/',views.contact, name='contact'),
    path('filtered_doctors/<dep_name>/',views.filtered_doctors, name='filtered_doctors'),
    path('single_doctor/<int:d_id>/',views.single_doctor, name='single_doctor'),
    path('sign_in/',views.sign_in, name='sign_in'),
    path('sign_up/',views.sign_up, name='sign_up'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('booking/<int:doctor_id>/', views.booking, name='booking'),
    path('save_contact/',views.save_contact, name='save_contact'),

]