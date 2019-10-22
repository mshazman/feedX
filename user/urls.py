from django.urls import path, include
from . import views as user_views

name = 'user'
urlpatterns = [
    path('', user_views.index, name='home'),
    path('register/', user_views.UserRegisterView.as_view(), name='register'),
    path('login/', user_views.UserLoginView.as_view(), name='login'),
    path('logout/', user_views.UserLogoutView.as_view(), name='logout'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('file/<str:filename>/<str:id>/<str:hex>', user_views.test),
    path('file/<str:filename>/<str:id>', user_views.test),
    path('file/<str:filename>', user_views.test),
]
