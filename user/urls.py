from django.urls import path,include
from . import views as user_views


name = 'user'
urlpatterns = [
    path('',user_views.index,name='home'),

]
