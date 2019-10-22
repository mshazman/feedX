"""feedX URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import handler500,handler404
from django.urls import path, include
from user import views as user_views
# from django.contrib.auth.views import password_reset, password_reset_done

urlpatterns = [
    path('',include('user.urls')),
    path('quiz/', include('quiz.urls')),
    path('user/',include('user.urls')),
    path('admin/', admin.site.urls),
    path('updateserver/', user_views.pull_url),
]
handler404 = user_views.handler404
handler500 = user_views.handler500
