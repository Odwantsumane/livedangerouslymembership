from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ProductsModel
from .forms import ProductsForm

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def products(request):
    template = loader.get_template('prod.html')
    return HttpResponse(template.render())

def details(request, id):
    mymember = Member.objects.all().get(id=id)
    template = loader.get_template('details.html')
    context = {
        "mymember":mymember,
    }
    return HttpResponse (template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return render(request, 'main.html',{})

def signup_user(request):
    template = loader.get_template('signup.html')
    mymembers = Member.objects.all().values()
    form = SignUpForm()
     
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            firstname = form.cleaned_data['first_name']
            # lastname = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            #authenticate
            user = authenticate(username=username,password=password)
            #login
            # print(firstname)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.success(request, ("There was an error logging in please try again!"))
                return redirect('/signup')
    context = {
        'form': form,
        'members':mymembers
    }
    return HttpResponse(template.render(context,request))

def login_user(request):
    template = loader.get_template('login.html')
    users = User.objects.all().values()
    mymembers = Member.objects.all().values()
    if (request.method == 'POST'):
        
        for i in users:
            if(i['email'] == request.POST['username']):
                username = User.objects.get(email=request.POST['username']).username
                break
            else:
                username ="wrongusername"

        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
         
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("There was an error logging in please try again!"))
            return redirect('login_user')
    context = {
        'members': mymembers,
    }
    return HttpResponse(template.render(context,request))

def logout_user(request):
    template = loader.get_template('logout.html')
    logout(request)
    messages.success(request,("you are logged out"))
    return redirect("/")

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry']
    }
    return HttpResponse(template.render(context, request))

def productItems(request):
    pm = ProductsModel.objects.all()
    form = ProductsForm()
    if(request.method == 'POST'):
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    return  render(request,'img.html',{'form':form})

 