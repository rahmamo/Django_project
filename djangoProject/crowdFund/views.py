from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect ,HttpResponse
from .models import Myuser,projects,imagesprject,TagProject
from .forms import *

def home(request):
    return render(request, 'home.html')

def surdeleteprofile(request):
    return render(request, 'surdelete.html')

def allproject(request):

    return render(request, 'surdelete.html')


def deleteprofile(request):
    Myuser.objects.filter(username=request.session['username']).delete()
    return redirect("/logout")

def myprofile(request):
    if (request.session.get('username') != None):
          return render(request, 'myprofile.html')
    else:
        return redirect("/log")

def Login(request):
    if (request.method == 'GET'):
        form = LForm()
        return render(request, 'login.html',{'form': form})
    else:
        user = Myuser.objects.filter(username=request.POST['username'], password=request.POST['password'])
        if user:
            request.session['id'] = user[0].id
            request.session['username'] = user[0].username
            request.session['first_name']=user[0].first_name
            request.session['last_name'] = user[0].last_name
            request.session['email']=user[0].email
            request.session['Birthdate']=str(user[0].Birthdate)
            request.session['phone_number']=user[0].phone_number
            request.session['profile_pic']=user[0].profile_pic.url
            request.session['country']=user[0].country
            request.session['facebook_profile']=user[0].facebook_profile
            return redirect("/home")
        else:
            form = LForm()
            return render(request, 'login.html', {'form': form})


def Register(request):
    if (request.method == 'GET'):
         form = RForm()
         return render(request, 'register.html',{'form': form})
    form = RForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'login.html')
    else:
        form = RForm()
        return render(request, 'register.html', {'form': form})






def updateprofile(request):
    if (request.session.get('username') != None):
        if (request.method == 'GET'):
            form = EForm()
            return render(request, 'updateprofile.html', {'form': form})
        else:
            form = EForm(request.POST, request.FILES)
            if form.is_valid():
                user = Myuser.objects.get(username=request.session['username'])
                form = EForm(request.POST, request.FILES, instance=user)
                form.save()
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['email'] = user.email
                request.session['Birthdate'] = str(user.Birthdate)
                request.session['phone_number'] = user.phone_number
                request.session['profile_pic'] = user.profile_pic.url
                request.session['country'] = user.country
                request.session['facebook_profile'] = user.facebook_profile
                return redirect("/myprofile")
            else:
                return HttpResponse("erorr")
    return redirect("/log")
def addimages(request):
    return HttpResponse("done")

def createproject(request):
    if (request.session.get('username') != None):
        if request.method == 'GET':
            form = CreateProject()
            return render(request, 'create_project.html', {'form': form})
        else:
            form = CreateProject(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                user = Myuser.objects.get(username=request.session.get('username'))
                project = projects.objects.get(title=request.POST['title'])
                if (project):
                    project.create = user.username
                    title = project.title
                    request.session['Project'] = project.title
                    project.save()
                else:
                    return render(request, 'project.html')
                return redirect("/choceproject")
    else:
        return redirect("/log")


def myProjects(request):
    if (request.session.get('username') != None):
        user = Myuser.objects.get(username=request.session.get('username'))
        project = projects.objects.filter(create=user.username)
        if project:
               context = {}
               context['projects'] = project
               return render(request, 'myproject.html', context)
        else:
            return  HttpResponse("not found project")
    else:
        return redirect("/log")

def addimage(request):
    if (request.session.get('username') != None):
        if request.method == 'GET':
            form = createImage()
            return render(request, 'addimage.html', {'form': form})
        else:
            form = createImage(request.POST, request.FILES)
            if form.is_valid():
                project = projects.objects.get(title=request.POST['nameproject'])
                print()
                if (project):
                    if (project.create == request.session.get('username')):
                               form.save()
                               return redirect("/choceproject")
                    else:
                        return HttpResponse("not found project")
                else:
                    return HttpResponse("not found project")
    else:
        return redirect("/log")


def choceproject(request):
    return render(request, 'project.html')

def addtag(request):
    if (request.session.get('username') != None):
        if request.method == 'GET':
            form = CreateTag()
            return render(request, 'addtag.html', {'form': form})
        else:
            form = CreateTag(request.POST, request.FILES)
            if form.is_valid():
                project = projects.objects.get(title=request.POST['nameproject'])
                print()
                if (project):
                    if (project.create == request.session.get('username')):
                               form.save()
                               return redirect("/choceproject")
                    else:return HttpResponse("not found project")
                else:
                    return HttpResponse("not found project")
    else:
        return redirect("/log")

def allProjects(request):
    project = projects.objects.all()
    context = {}
    context['projects'] = project
    return render(request, 'allProjects.html', context)


def viewProjects(request, projectTitle):
    project = projects.objects.get(title=projectTitle)
    context = {}
    context['projects'] = project
    imgproject = imagesprject.objects.filter(nameproject=projectTitle)
    context['imgprojects'] = imgproject

    Tagprojects = TagProject.objects.filter(nameproject=project.title)
    for Tagproject in Tagprojects:
        similar = TagProject.objects.filter(tags=Tagproject.tags)
        context['similars'] = similar

    return render(request, 'viewproject.html', context)
