from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Profile

# Create your views here.
def create_account(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        account = Profile.objects.create(
            hood = data['hood'],
            location = data['location'],
            bio = data['bio'],
            image =image,
            user = request.user
        )
        return redirect('login')
    return render(request,template_name="main/create.html")
@login_required(login_url='login')
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