from django.db import models

# Create your models here.
class Member (models.Model):
    userId = models.IntegerField(null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    date = models.DateField(null=True)
    username = models.EmailField(null=True)
    password = models.CharField(max_length=30, null=True)
    nofms = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class ProductsModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/buygear")
    manudate = models.DateField(max_length=200)
    modeltype = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.title