from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request,'webApp/home.html')

def service(request):
    return render(request,'webApp/service.html')

def store(request):
    return render(request,'webApp/store.html')

def blog(request):
    return render(request,'webApp/blog.html')

def contact(request):
    return render(request,'webApp/contact.html')
    