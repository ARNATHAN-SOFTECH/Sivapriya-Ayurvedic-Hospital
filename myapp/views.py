from django.shortcuts import get_object_or_404, render
from .models import Doctor

def doctors(request):
    doctors = Doctor.objects.filter(available=True)
    return render(request, 'doctors.html', {
        'doctors': doctors
    })

def home(request):
    return render(request, 'home.html')
def treatments(request):
    return render(request, 'treatments.html')



def doctor_detail(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    return render(request, 'doctor_detail.html', {
        'doctor': doctor
    })


def contact(request):
    return render(request, 'contact.html')
