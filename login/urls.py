from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='login-index'),
    path('logout', views.logoutView, name='logout-index'),
    path('admin', views.adminLogin, name='admin-login'),
]


    # path('password-reset/', av.PasswordResetView.as_view(template_name='login/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', av.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', av.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset-complete/', av.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete')