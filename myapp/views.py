from django.shortcuts import get_object_or_404, render
from .models import Doctor
from .models import Gallery

def gallery(request):
    images = Gallery.objects.all().order_by('-created_at')

    return render(
        request,
        'gallery.html',
        {
            'images': images
        }
    )
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

def about(request):
    return render(request, "about.html")
