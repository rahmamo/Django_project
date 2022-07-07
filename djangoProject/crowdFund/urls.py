"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import Login,Register,home,Register,myprofile,updateprofile,\
    deleteprofile,surdeleteprofile,createproject,myProjects,addimage,choceproject,addtag,allProjects,viewProjects,\
    rateProject,donate,commentproject,reportcomment,reportproject,cancel,projectCategorie,searchtage,highestRate,verify

urlpatterns = [
    path('home', home),
    path('Register',Register),
    path('log', Login),
    path('myprofile',myprofile),
    path('updateprofile',updateprofile),
    path('deleteprofile',deleteprofile),
    path('surdeleteprofile',surdeleteprofile),
    path('createproject',createproject),
    path('myProjects',myProjects),
    path('addimage',addimage),
    path('choceproject',choceproject),
    path('addtag', addtag),
    path('allProjects', allProjects),
    path('viewProjects/<projectTitle>', viewProjects),
    path('rateProject/<projectTitle>/<int:rate>', rateProject),
    path('donate/<projectTitle>',donate),
    path('commentproject/<title>',commentproject),
    path('reportcomment/<id>/<title>',reportcomment),
    path('reportproject/<title>',reportproject),
    path('cancel/<title>',cancel),
    path('projectCategorie/<name>',projectCategorie),
    path('searchtage',searchtage),
    path('highestRate', highestRate),
    path('verify/<str:token>',verify),
    path('logout', LogoutView.as_view(template_name='log_out.html')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
