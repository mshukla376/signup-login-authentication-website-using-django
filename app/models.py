from django.db import models

class signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static')
