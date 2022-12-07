from django.contrib import admin
from .models import new_user

# Register your models here.
class Book(admin.ModelAdmin):
    list_display = ('id','username','email','password','phone','place')
admin.site.register(new_user, Book)
