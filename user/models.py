from django.db import models


# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=200)
    tel = models.CharField(max_length=11)
    email = models.EmailField(default='aaaa@gmail.com')
    sex = models.BooleanField(default=True)
    age = models.IntegerField(default=10)
    img = models.ImageField(upload_to='photo/',default='default/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.BooleanField(default=False)


