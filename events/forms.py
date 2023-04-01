from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image, Image_camping, Image_skydiving, Image_canoeing, Image_hiking, Image_campingg, Image_skydivingg, Image_canoeingg, Image_hikingg
from .models import Messages
# from .models import ProductsModel
# class messageForm():

#     class Meta:
#         model = 
# class ProductsForm(forms.ModelForm):
#     class Meta:
#         model = ProductsModel
#         fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('message',)
class ImageFormCamping(forms.ModelForm):
    class Meta:
        model = Image_camping
        fields = ('title','labels', 'descrip', 'image')

class ImageFormSkydiving(forms.ModelForm):
    class Meta:
        model = Image_skydiving
        fields = ('title','labels', 'descrip', 'image')

class ImageFormCanoeing(forms.ModelForm):
    class Meta:
        model = Image_canoeing
        fields = ('title','labels', 'descrip', 'image')

class ImageFormHiking(forms.ModelForm):
    class Meta:
        model = Image_hiking
        fields = ('title','labels', 'descrip', 'image')

class ImageFormCampingg(forms.ModelForm):
    class Meta:
        model = Image_campingg
        fields = ('title', 'image')

class ImageFormSkydivingg(forms.ModelForm):
    class Meta:
        model = Image_skydivingg
        fields = ('title', 'image')

class ImageFormCanoeingg(forms.ModelForm):
    class Meta:
        model = Image_canoeingg
        fields = ('title', 'image')

class ImageFormHikingg(forms.ModelForm):
    class Meta:
        model = Image_hikingg
        fields = ('title', 'image')

