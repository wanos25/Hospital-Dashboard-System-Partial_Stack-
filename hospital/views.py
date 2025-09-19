from django.shortcuts import render

def home(request):
    return render(request, "Futuristic-Hospital-Dashboard.html")
