# Ex02 Django ORM Web Application
## Date: 12.02.24

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class football (models.Model):
   matches =models.IntegerField()
   name=models.CharField(max_length=100)
   prizes =models.IntegerField()
   age=models.IntegerField()
   email=models.EmailField()
class footballAdmin(admin.ModelAdmin):
   list_display=('matches','name','prizes','age','email')

admin.py
from django.contrib import admin
from .models import football,footballAdmin
admin.site.register(football,footballAdmin)
```

## OUTPUT
![Alt text](<Screenshot (1).png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
