from django.urls import path
from . import views
from django.contrib.auth import views as av
urlpatterns = [
    path('', views.index, name='frontpage-index'),
    path('password-reset/', av.PasswordResetView.as_view(template_name='login/password_reset.html'), name='password_reset'),
    path('password-reset/done/', av.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', av.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', av.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete')

]


