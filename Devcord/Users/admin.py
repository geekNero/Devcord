from django.contrib import admin
from django.db import models
from .models import *
# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=["user","friends","requests"]
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display=["name"]
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display=["name"]
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display=["domain","software","player"]
@admin.register(FrameWork_or_Platform)
class FrameWork(admin.ModelAdmin):
    list_display=["name"]