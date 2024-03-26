# Ex02 Django ORM Web Application
## Date: 12.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

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
Execute Django admin and create details for 10 books

## PROGRAM
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

## OUTPUT
![Screenshot (1)](https://github.com/samsonsamuel02/ex2/assets/147018611/a0655db5-7a8e-43b1-b394-1ed1a47be41b)





## RESULT
Thus the program for creating a database using ORM hass been executed successfully
