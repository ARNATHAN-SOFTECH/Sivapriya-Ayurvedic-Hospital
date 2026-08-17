from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def treatments(request):
    return render(request, 'treatments.html')