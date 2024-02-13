from django.contrib import admin
from .models import MY_MO
# Register your models here.
@admin.register(MY_MO)
class Admin(admin.ModelAdmin):
    list_display = ['id','name','email','password']