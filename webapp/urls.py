from django.urls import path
from webapp import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('all_departments/',views.all_departments, name='all_departments'),
    path('doctors/',views.doctors, name='doctors'),
    path('contact/',views.contact, name='contact'),

]