from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#django ko user table le username ra password magxa tara hami email ra password magne banauxau
class User(AbstractUser):
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default ='username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Category(models.Model):
    name = models.CharField(max_length = 100)

class Ingredient(models.Model):
    name =models.CharField(max_length = 100)

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    ingredients = models.ManyToManyField(Ingredient)
    process = models.TextField()
    description = models.TextField()
    picture = models.ImageField(upload_to='Recipe_pics',blank = True, null = True)
