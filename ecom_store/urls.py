from django.urls import path
from ecom_store.views.ecom_authentication import register_view, login_view, logout_view
from ecom_store.views.views import home
from ecom_store.views.ecom_password import (
    ChangePassword,
    # ChangePasswordDone,
    PasswordReset,
    # PasswordResetDone,
    PasswordResetConfirm,
    # PasswordResetComplete
)
from ecom_store.views.ecom_profile import user_profile, edit_user_profile

urlpatterns = [
    path('', home, name='home'),

    # Registration
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Password Change
    path('password_change/', ChangePassword.as_view(), name='password_change'),
    # path('password_change/done/', ChangePasswordDone.as_view(), name='password_change_done'),

    # Password Reset
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    # path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),

    # Profile
    path('profile', user_profile, name='profile'),
    path('profile/edit/', edit_user_profile, name='edit_profile'),
]
