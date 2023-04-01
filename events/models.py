from django.db import models


# Create your models here.
class Messages (models.Model):
    headImage = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.CharField(max_length=255, null=True)
    message = models.TextField(max_length=255)

class Image(models.Model):
    userId = models.IntegerField(null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

class Image_camping(models.Model):
    title = models.CharField(max_length=200)
    labels = models.CharField(max_length=200, null=True)
    descrip = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/camping/")
    

    def __str__(self):
        return self.title

class Image_skydiving(models.Model):
    title = models.CharField(max_length=200)
    labels = models.CharField(max_length=200, null=True)
    descrip = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/skydiving/")
    

    def __str__(self):
        return self.title
    
class Image_canoeing(models.Model):
    title = models.CharField(max_length=200)
    labels = models.CharField(max_length=200, null=True)
    descrip = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/canoeing/")
    

    def __str__(self):
        return self.title

class Image_hiking(models.Model):
    title = models.CharField(max_length=200)
    labels = models.CharField(max_length=200, null=True)
    descrip = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/hiking/")
    

    def __str__(self):
        return self.title
    
class Image_hikingg(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/hiking/gear/")

    def __str__(self):
        return self.title

class Image_canoeingg(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/canoeing/gear/")

    def __str__(self):
        return self.title
    
class Image_skydivingg(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/skydiving/gear/")

    def __str__(self):
        return self.title
    
class Image_campingg(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/camping/gear/")

    def __str__(self):
        return self.title
    
# class ProductsModel(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(null=True, blank=True, upload_to="images/buygear")
#     manudate = models.DateField(max_length=200)
#     modeltype = models.CharField(max_length=200)
#     brand = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title
    