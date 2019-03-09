from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Wrapper.html")
def register(request):
    return render(request, "register.html")