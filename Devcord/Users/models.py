from django.db import models
from django.contrib.auth.models import User
import datetime
class Player(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    friends=models.TextField(null=True)
    requests=models.TextField(null=True)
    # software = models.CharField(
    #     max_length=10,
    #     null=True,
    #     choices=(
    #         ("code","VS Code"),
    #     ),
    # ) 
    # domain = models.CharField(
    #     max_length=10,
    #     null=True,
    #     choices=(
    #         ("Web Dev","Web Development"),
    #     ),
    # ) 
    # login_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    # logout_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.user.username
class Software(models.Model):
    name=models.CharField(max_length=1003, null=True)
    executable=models.CharField(max_length=1003, null=True)
    def __str__(self):
        return self.name
class Domain(models.Model):
    name= models.CharField(max_length=1003, null=True)
    software=models.ManyToManyField(Software)
    def __str__(self):
        return self.name
class FrameWork_or_Platform(models.Model):
    name= models.CharField(max_length=1003, null=True)
    domain= models.ForeignKey(Domain,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Session(models.Model):
    login_time=models.DateTimeField(auto_now=False, auto_now_add=False,default=datetime.datetime.now())
    logout_time=models.DateTimeField(auto_now=False, auto_now_add=False,default=datetime.datetime.now())
    domain=models.ForeignKey(Domain,null=True,on_delete=models.CASCADE)
    software=models.ForeignKey(Software,null=True,on_delete=models.CASCADE)
    frameWork_or_platform=models.ForeignKey(FrameWork_or_Platform,null=True,on_delete=models.CASCADE)
    player=models.ForeignKey(Player,null=True,on_delete=models.CASCADE)
