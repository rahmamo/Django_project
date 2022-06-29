from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect ,HttpResponse
from .models import Myuser

def home(request):
    return HttpResponse("report list student HttpResponse")
def Login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:
        user = Myuser.objects.filter(username=request.POST['username'], password=request.POST['password'])
        if user:
            request.session['loginid'] = user[0].id
            request.session['username'] = user[0].username
            print(request.session['username'])
            return HttpResponse("report list student HttpResponse")

        else:
            return HttpResponse("notfound")


def Register(request):

    if (request.method == 'GET'):
         return render(request, 'register.html')
    user = Myuser.objects.filter(username=request.POST['username'], password=request.POST['password'])
    if user:
        return render(request, 'register.html',{'error':'user exists'})
    else:
        Myuser.objects.create(username=request.POST['username'],password=request.POST['password'] ,email=request.POST['email'],
                              first_name=request.POST['first_name'],last_name=request.POST['last_name']
                              ,phone_number=request.POST['phone_number'],profile_pic = request.POST['profile_pic'])
        # profile_pic = request.POST['profile_pic']
        return render(request, 'login.html')
