from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('login/register_user/', register, name='register_user'),
    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('profile/', dashboard_view, name='user_profile'),
    path('profile/edit', edit_user, name='edit_user_information'),
    path('signup/', user_register, name='user_register'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout1/', logoutpage, name="logout"),
    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('profile/', dashboard_view, name='user_profile'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
