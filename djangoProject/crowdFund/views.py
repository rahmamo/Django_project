from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect ,HttpResponse
from .models import Myuser,projects,imagesprject,TagProject,Comment,CommentReports,ProjectReports,Categories,CategoriesProject
from .forms import *
import random
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    if (request.session.get('username') != None):
        Categorie = CategoriesProject.objects.all()
        context = {}
        context['Categories'] = Categorie
        project = projects.objects.all().order_by('-project_id')[:5]
        context['projects'] = project
        return render(request, 'home.html',context)
    else:
        return redirect("/logout")

def searchtage(request):
    if (request.method == 'GET'):
         return redirect("/home")
    else:
        namep=request.POST['search']
        projectTitle=projects.objects.filter(title=namep)
        if projectTitle:
            return HttpResponseRedirect("/viewProjects/" + projectTitle.title)
        else :
            Tagproject = TagProject.objects.filter(tags=namep)
            if Tagproject :
                context={}
                context['Tagprojects']=Tagproject
                return render(request,'projectTage.html',context)
            else:
                return render(request,'notfound.html')




def projectCategorie(request,name):
    if (request.session.get('username') != None):
        project = projects.objects.filter(category=name)
        context={}
        context['projects'] = project
        return render(request, 'categories.html',context)
    else:
        return redirect("/logout")



def surdeleteprofile(request):
    if (request.session.get('username') != None):
        return render(request, 'surdelete.html')
    else:
        return redirect("/logout")

def allproject(request):
    if (request.session.get('username') != None):
         return render(request, 'surdelete.html')
    else:
        return redirect("/logout")

def deleteprofile(request):
    Myuser.objects.filter(username=request.session['username']).delete()
    return redirect("/logout")

def myprofile(request):
    if (request.session.get('username') != None):
          user = Myuser.objects.get(username=request.session.get('username'))
          context = {}
          context['user']=user
          return render(request, 'myprofile.html',context)
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
    commit=Comment.objects.filter(title=projectTitle)
    context = {}
    context['projects'] = project
    context['commits']=commit
    imgproject = imagesprject.objects.filter(nameproject=projectTitle)
    context['imgprojects'] = imgproject
    Tagprojects = TagProject.objects.filter(nameproject=project.title)
    for Tagproject in Tagprojects:
        similar = TagProject.objects.filter(tags=Tagproject.tags)
        context['similars'] = similar

    return render(request, 'viewproject.html', context)


def rateProject(request, projectTitle, rate):
    project = projects.objects.get(title=projectTitle)
    project.Rating = project.Rating + rate
    project.save()
    return HttpResponseRedirect("/viewProjects/"+project.title)



def donate(request,projectTitle):
    if(request.method == 'POST'):
        donate = request.POST['donate']
        project = projects.objects.get(title=projectTitle)
        user=Myuser.objects.get(username=request.session.get('username'))
        donateuser = int(user.donations) + int(donate)
        donateproject = int(project.donations) + int(donate)
        project.donations = project.donations + donateproject
        user.donations = user.donations + donateuser
        project.save()
        user.save()
        return HttpResponseRedirect("/viewProjects/"+project.title)
    return HttpResponse("error")

def commentproject(request, title):
    if (request.method == 'POST'):
           project=projects.objects.get(title=title)
           Comment.objects.create(title=title,comment=request.POST['comment'],username=request.session.get('username')) ###############  user_id_id=request.session.get('id')
           return HttpResponseRedirect("/viewProjects/"+project.title)
    else:
        return redirect("/log")
def reportcomment(request, id,title):
    print(id)
    print(title)
    project = projects.objects.get(title=title)
    CommentReports.objects.create(comment_id=id,username=request.session.get('username'))
    return HttpResponseRedirect("/viewProjects/" + project.title)

def reportproject(request,title):
    if (request.method == 'POST'):
        project = projects.objects.get(title=title)
        message=request.POST['report']
        ProjectReports.objects.create(title=title,message=message, username=request.session.get('username'))
        return HttpResponseRedirect("/viewProjects/" + project.title)
    else:
        return render(request,'reportproject.html')

def cancel(request, title):
    project = projects.objects.get(title=title)
    dalete = project.donations/project.total_target
    if( dalete < 0.25):
        project.delete()
        return HttpResponseRedirect("/home")
    else:
        return HttpResponse("can not delete")
def highestRate(request):
    highestRate = projects.objects.all().order_by('Rating')[:5]
    # highestRate = projects.objects.filter(
    #    avg_rate__gte =projects.objects.order_by('avg_rate')[4].avg_rate
    #  ).order_by('avg_rate')
    context = {}
    context['projects'] = highestRate
    return render(request, 'home.html', context)
# def maxhighestRate(request):
#     maxhighestRate = projects.objects.all().aggregate(max("avg_rate"))[:5]
#
#     print(maxhighestRate)
#     return render(request, 'home.html', {'highestRate':highestRate})
#-----------------------Email Verification---------------
# def Register(request):
#     form = RForm()
#     if (request.method == 'POST'):
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         user = Myuser(username=username,email=email)
#         domain_name = get_current_site(request).domain
#         token= str(random.random()).split('.')[1]
#         user.token =token
#         link = f'http://{domain_name}/verify/{token}'
#         send_mail(
#             'Email Verification',
#             f'please click this link {link} to verify your email',
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently=False,
#         )
#         return HttpResponse('the email has be sent')
#     return render(request,'login.html',{'form': form})
#
# def verify(request,token):
#     try:
#         user=Myuser.objects.filter(token = token)
#         if user:
#             user.is_verified = True
#             msg = "your email has been verified"
#             return render(request,'verify.html',{'msg': msg})
#     except Exception as e:
#         msg : e
#         return render(request,'verify.html',{'msg':e})
