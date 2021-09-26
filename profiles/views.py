from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Profile,Business,Amenity,Post,Like

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
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('post_pic')
        
        post = Post.objects.create(
            image = image,
            description = data['post_data'],
            user = request.user,
        )
        return redirect('dash')
    person=request.user.pk
    posts = Post.objects.all()
    profile = Profile.objects.filter(user=person).all()
    ctx = {"profile":profile,"posts":posts}
    return render(request,"main/dashboard.html",ctx)
@login_required(login_url='login')
def personal(request):
    person=request.user.pk
    profile = Profile.objects.filter(user=person).all()
    biz = Business.objects.filter(owner=person).all()
    ctx = {"profile":profile,"biz":biz}
    return render(request,"main/profile.html",ctx)
@login_required(login_url='login')
def business(request):
    person=request.user.pk
    profile = Profile.objects.filter(user=person).all()
    ctx = {"profile":profile}
    return render(request,template_name="main/business.html")
def b_search(request):
    return render(request,template_name="main/search.html")
@login_required(login_url='login')
def amenities(request):
    person=request.user.pk
    amen = Amenity.objects.all()
    profile = Profile.objects.filter(user=person).all()
    ctx = {"amen":amen,"profile":profile,}
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

def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user,post_id=post_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like' 
        like.save()           
    return redirect('dash')