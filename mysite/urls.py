"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from login import views
from article.views import add_article, modify_article, myarticles, mypills, articledetail, pilldetail
from article.views import pron
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls')),
    path('confirm/', views.user_confirm),
    path('articles/', add_article),
    path('articles/<int:art_id>', modify_article),
    path('myarticles/', myarticles),
    path('mypills/', mypills),
    path('articledetail/<int:art_id>', articledetail),
    path('pilldetail/<int:art_id>', pilldetail),
    path('pron/', pron)
]
