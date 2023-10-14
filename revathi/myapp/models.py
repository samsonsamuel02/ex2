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