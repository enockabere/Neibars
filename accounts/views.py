from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import  login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import message, send_mail
from django.conf import settings

# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            subject = "Welcome to Neibars!"
            sender = settings.EMAIL_HOST_USER
            message = f"Hello {username} Welcome to the Neibars You will find the most exciting insights about your hood."
            recipients_list = [email]
            send_mail(subject,message,sender,recipients_list,fail_silently=False)
            user =form.save()
            login(request,user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})
