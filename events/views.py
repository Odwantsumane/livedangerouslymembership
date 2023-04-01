from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from django.contrib.auth.models import User
from .models import Messages, Image
from members.models import Member
from .forms import ImageForm, ImageFormCamping , ImageFormSkydiving, ImageFormCanoeing, ImageFormHiking, ImageFormCampingg , ImageFormSkydivingg, ImageFormCanoeingg, ImageFormHikingg
from .forms import MessageForm
# Create your views here.
deleted = False

def home(request):
    template = loader.get_template('main.html')
    return render(request, 'main.html')

def products(request):

    context = {
        'cam': True,
        'can': True,
        'hik': True,
        'sky': True,
    }
    
    return render(request, 'prod.html', context)

def chat(request): #will add id
    users = User.objects.all().values()
    current_user = request.user
    message = Messages.objects.all()
    imageIcon = Image.objects.all()[0].image
    indicate = True
    
    current_user_l_name = User.objects.get(id=current_user.id).last_name
    current_user_f_name = User.objects.get(id=current_user.id).first_name
    decrnms(request) 
    form = MessageForm()
    if(request.method == 'POST'):
        form = MessageForm(request.POST, request.FILES)
        # ms = request.POST['message']
        if form.is_valid():
            form.save()
            incrnms(request)
            m = Messages.objects.all()[len(Messages.objects.all())-1]
            for i in Image.objects.all():
                if(current_user.id == i.userId):
                    m.headImage = i.image
                    m.save()
                    indicate = False
                    break
            if(indicate):
                m.headImage = imageIcon
                m.save()

            m.author = current_user_f_name+" "+current_user_l_name
            m.save()
        
    context = {
        'users': users,
        'messages': message,
        'form': form,
    }
    # form = messageForm()
    return render(request, 'chat.html',context)



def delete(request, id):
    users = User.objects.all().values()
    form = MessageForm()
    messages = Messages.objects.all()
    delete = False
    deleteUn = False

    message = Messages.objects.get(id=id)
    fullname = request.user.first_name + " "+ request.user.last_name
    if (request.user.is_superuser):
        delete = True
        message.delete()
    elif(fullname == message.author):
        delete = True
        message.delete() # delete message
    else:
        #unauthorized delete
        deleteUn = True,
        

    context = {
        'users': users,
        'messages': messages,
        'delete_success': delete,
        'unauthorized_delete': deleteUn,
        
    }
    return render(request, 'chat.html',context)
    
def incrnms(request):
    
    currentUser = request.user.id
    members = Member.objects.all()
    for i in members:
        if(i.userId != currentUser):
            conc = i.nofms + 1
            i.nofms = conc
            i.save()
             
def decrnms(request):
    currentUser = request.user.id
    members = Member.objects.all()
    # Member.objects.get(userId=currentUser).nofms = 0
    # Member.objects.get(userId=currentUser).save()
    for i in members:
        if(i.userId == currentUser):
            conc = 0
            i.nofms = conc
            i.save()

def images(request):
    # img = Image.objects.all().values()
    current_user = request.user
    indicate = True
 
    if(request.method == 'POST'):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            for i in Image.objects.all():
                if(current_user.id == i.userId):
                    i.image = request.FILES['image'] #nedd to update the image
                    i.save()
                    indicate = False

                    break
            if(indicate):
                form.save()
                update_u_id = Image.objects.all()[len(Image.objects.all().values())-1]
                update_u_id.userId = current_user.id
                update_u_id.save()
            print(Image.objects.all().values())
            #get the current instance object to display in the template
            img_obj = form.instance
            return render(request, "img.html", {'img_obj':img_obj, 'form':form})
    else:
        form = ImageForm() 
    return render(request,'img.html',{'form':form})

def camping(request):
    form = ImageFormCamping()
    if(request.method == 'POST'):
        form = ImageFormCamping(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            img_obj = form.instance
            return redirect('/')
            # return render(request, "main.html", {'img_obj':img_obj, 'formcam':form})
    return render(request,'main.html',{'formcam':form})

def canoeing(request):
    form = ImageFormCanoeing()
    if(request.method == 'POST'):
        form = ImageFormCanoeing(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            img_obj = form.instance
            return redirect('/')
            # return render(request, "main.html", {'img_obj':img_obj, 'formcan':form})

    return render(request,'main.html',{'formcan':form})

def hiking(request):
    form = ImageFormHiking()
    if(request.method == 'POST'):
        form = ImageFormHiking(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            img_obj = form.instance
            return redirect('/')
            #return render(request, "main.html", {'img_obj':img_obj, 'formhki':form})
    return render(request,'main.html',{'formhki':form})

def skydiving(request):
    form = ImageFormSkydiving()
    if(request.method == 'POST'):
        form = ImageFormSkydiving(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            img_obj = form.instance
            return redirect('/')
            # return render(request, "main.html", {'img_obj':img_obj, 'formsky':form})
    return render(request,'main.html',{'formsky':form})

def gearup(request):
    return render(request, 'gearup.html',{})

def campingGear(request):
    form = ImageFormCampingg()
    if(request.method == 'POST'):
        form = ImageFormCampingg(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('gearup')
    return render(request, 'gearup.html', {'form1':form})

def hikingGear(request):
    form = ImageFormHikingg()
    if(request.method == 'POST'):
        form = ImageFormHikingg(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('gearup')
    return render(request, 'gearup.html', {'form2':form})

def canoeingGear(request):
    form = ImageFormCanoeingg()
    if(request.method == 'POST'):
        form = ImageFormCanoeingg(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('gearup')
    return render(request, 'gearup.html', {'form3':form})

def skydivingGear(request):
    form = ImageFormSkydivingg()
    if(request.method == 'POST'):
        form = ImageFormSkydivingg(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('gearup')
    return render(request, 'gearup.html', {'form4':form})

def cart(request):

    return render(request, 'cart.html', {})

def campprod(request):
    return render(request,'prod.html', {'cam': True})

def canprod(request):
    return render(request,'prod.html', {'can': True})

def hikprod(request):
    return render(request,'prod.html', {'hik': True})

def skyprod(request):
    return render(request,'prod.html', {'sky': True})