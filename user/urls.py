from django.urls import path, include
from . import views as user_views
from django.contrib.auth import views as auth_views

name = 'user'
urlpatterns = [
    path('', user_views.index, name='home'),
    path('register/', user_views.UserRegisterView.as_view(), name='register'),
    path('login/', user_views.UserLoginView.as_view(), name='login'),
    path('logout/', user_views.UserLogoutView.as_view(), name='logout'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('reset-password',user_views.UserPasswordResetView.as_view(),name='password_reset'),
    path('reset-password/done/',user_views.UserPasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset-password/done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
    name='password_reset_complete'),
    path('email',user_views.email,name='email'),
    path('file/<str:filename>/<str:id>/<str:hex>',user_views.test),
    path('file/<str:filename>/<str:id>',user_views.test),
    path('file/<str:filename>',user_views.test)
]
