from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Profile,Business,Amenity

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
def sidebar(request):
    person=request.user.pk
    profile = Profile.objects.filter(user=person).all()
    ctx = {"profile":profile}
    return render(request,"sidebar.html",ctx)
@login_required(login_url='login')
def dashboard(request):
    return render(request,template_name="main/dashboard.html")
@login_required(login_url='login')
def personal(request):
    person=request.user.pk
    profile = Profile.objects.filter(user=person).all()
    biz = Business.objects.filter(owner=person).all()
    ctx = {"profile":profile,"biz":biz}
    return render(request,"main/profile.html",ctx)
def business(request):
    return render(request,template_name="main/business.html")
def b_search(request):
    return render(request,template_name="main/search.html")
def amenities(request):
    amen = Amenity.objects.all()
    ctx = {"amen":amen}
    return render(request,"main/amenities.html",ctx)
def create_biz(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('b_pic')
        biz = Business.objects.create(
            name = data['b-name'],
            image = image,
            location = data['b-location'],
            info = data['b-info'],
            owner = request.user
        )
    return redirect('personal')
def create_amenity(request):
    if request.method == 'POST':
        data = request.POST
        amenity = Amenity.objects.create(
            types = data['a-type'],
            contacts = data['a-contact'],
            info = data['a-info'],
            user = request.user
        )
    return redirect('personal')