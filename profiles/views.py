from django.shortcuts import render

# Create your views here.
def create_account(request):
    return render(request,template_name="main/create.html")
def dashboard(request):
    return render(request,template_name="main/dashboard.html")
def personal(request):
    return render(request,template_name="main/profile.html")
def business(request):
    return render(request,template_name="main/business.html")
def b_search(request):
    return render(request,template_name="main/search.html")
def amenities(request):
    return render(request,template_name="main/amenities.html")