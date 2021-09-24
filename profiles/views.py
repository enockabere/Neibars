from django.shortcuts import render

# Create your views here.
def create_account(request):
    return render(request,template_name="main/register.html")