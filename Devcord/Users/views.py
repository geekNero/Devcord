from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
import datetime
def login(request):
    if request.method == "POST":
        if(request.user.is_authenticated):
            return redirect("home")
        else:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    print(user)
                    auth_login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    try:
                        nw=Player(user=user,friends="")
                        nw.save()
                    except:
                        pass
                    return redirect("selector")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})
# Create your views here.
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, template_name="register.html" ,context={"register_form":form})
@login_required
def home(request):
    obs=User.objects.all()
    player=Player.objects.get(user=request.user)
    req=player.requests
    arr=[]
    for i in range(0,len(req),5):
        s=req[i:i+5]
        a=int(s)
        if(a!=0):
            arr.append(User.objects.get(id=a))
    friends=[]
    friends_code=player.friends
    for i in range(0,len(friends_code),5):
        s=req[i:i+5]
        a=int(s)
        if(a!=0 and User.objects.get(id=a).is_authenticated()):
            friends.append(Player.objects.get(user=User.objects.get(id=a)))
    return render(request,'home.html',{"users":obs,"requests":arr,"friends":friends})
@login_required
def logout_view(request):
    nw=Player.objects.get(user=request.user)
    nw.logout_time=datetime.datetime.now()
    nw.save()
    logout(request)
    return render(request,'logout.html',{'users':"HeLLO"})
@login_required
def search(request):
    if(request.method=="POST"):
        res=request.POST['res']
        return redirect('profile',res)
@login_required
def remove(request,username):
    a=Player.objects.get(user=request.user)
    valar=User.objects.get(username=username)
    b=Player.objects.get(user=valar)
    s=str(a.friends)
    si=str(b.friends)
    fin=str(valar.id)
    fines=str(request.user.id)
    sr=""
    for i in range(0,len(s),5):
        if(fin==s[i:i+5]):
            sr=s[:i]
            if(i+5<=len(s)):
                sr+=s[i+5:]
    print(s,sr,"fi")
    a.friends=sr
    a.save()
    for i in range(0,len(si),5):
        if(fines==si[i:i+5]):
            sr=si[:i]
            if(i+5<=len(si)):
                sr+=s[i+5:]
    print(si,sr,"fines")
    b.friends=sr
    b.save()
    return redirect('profile',username)
@login_required
def accept(request,username):
    valar=User.objects.get(username=username)
    a=Player.objects.get(user=valar)
    s=str(request.user.id)
    f=str(a.friends)
    while(len(s)<5):
        s="0"+s
    f+=s
    a.friends=f
    a.save()
    print(a.friends)
    b=Player.objects.get(user=request.user)
    s=str(b.friends)
    f=str(valar.id)
    while(len(f)<5):
        f="0"+f
    s+=f
    b.friends=s
    b.save()
    print(b.friends)
    s=str(valar.id)
    f=str(b.requests)
    while(len(s)<5):
        s="0"+s
    str1=""
    for i in range(0,len(f),5):
        if(f[i:i+5]==s):
            str1=f[:i]
            if(i+5<len(f)):
                str1+=f[i+5:]
    b.requests=str1
    b.save()
    return redirect('profile',username)
@login_required
def cancel_request(request,username):
    print('In Cancel Request')
    valar=User.objects.get(username=username)
    a=Player.objects.get(user=valar)
    s=str(request.user.id)
    f=str(a.requests)
    while(len(s)<5):
        s="0"+s
    str1=""
    for i in range(0,len(f),5):
        if(f[i:i+5]==s):
            str1=f[:i]
            if(i+5<len(f)):
                str1+=f[i+5:]
    a.requests=str1
    a.save()
    return redirect('profile',username)
@login_required
def add_friend(request,username):
    print(request.user,username )
    valar=User.objects.get(username=username)
    a=Player.objects.get(user=valar)
    s=str(request.user.id)
    f=str(a.requests)
    while(len(s)<5):
        s="0"+s
    f+=s
    a.requests=f
    a.save()
    return redirect('profile',username)
@login_required
def profile(request,username):
    try:
        valar=User.objects.get(username=username)
    except:
        return render(request, 'user_does_not_exist.html')
    if(request.user.username!=valar.username):
        a=Player.objects.get(user=valar)
        s=""
        check=str(Player.objects.get(user=request.user).friends)
        check2=str(a.requests)
        f=str(valar.id)
        while(len(f)<5):
            f="0"+f
        val=-1
        for i in range(0,len(check),5):
            print(check[i:i+5],f)
            print('Friends Area')
            if(check[i:i+5]==f):
                val=1
                break
        print(val)
        if(val==1):
            s="Remove Friend"
        else:
            f=str(request.user.id)
            while(len(f)<5):
                f='0'+f
            for i in range(0,len(check2),5):
                print(check2[i:i+5],f)
                if(check2[i:i+5]==f):
                    print('Request Area')
                    s="Cancel Request"
                    break
            else:
                s="Send Request"
        return render(request,'profile.html',{'user':valar,'friend':s})
    else:
        return render(request,'profile.html',{'user':valar})
# @login_required
# def session(request):
#     pass
@login_required
def selector(request):
    software=list(Software.objects.all())
    dict={}
    for soft in software:
        dict[soft]=list(Domain.objects.filter(software=soft))
    dict=[dict]
    print(dict[0])

    return render(request,'session.html',{"software":software,"dict":dict,"length":len(software)})


