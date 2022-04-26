from django.contrib import admin
from django.db import models
from .models import *
# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=["user","friends","requests"]