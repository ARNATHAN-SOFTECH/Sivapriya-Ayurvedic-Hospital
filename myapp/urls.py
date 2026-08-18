from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('treatments/', views.treatments, name='treatments'),

    path('doctors/<slug:slug>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/', views.doctors, name='doctors'),
    
    path('contact/', views.contact, name='contact'),
    path("about/",views.about, name="about"),
]