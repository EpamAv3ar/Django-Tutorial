from django.contrib.auth.views import (
PasswordChangeView,
PasswordChangeDoneView,
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

class ChangePassword(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy('home')
    # extra_context = {}

    def form_valid(self, form):
        messages.success(self.request, "Your password has been changed successfully.")
        return super().form_valid(form)

# class ChangePasswordDone(PasswordChangeDoneView):
#     template_name = 'password/password_change_done.html'
    # extra_context = {}

class PasswordReset(PasswordResetView):
    template_name = 'password/password_reset.html'
    success_url = reverse_lazy('home')
    # email_template_name = ""
    # subject_template_name = ""
    # html_email_template_name = ""
    # from_email = ""
    # extra_email_context = ""
    # token_generator = ""
    # form_class = ""
    # extra_context = ""

    def form_valid(self, form):
        messages.success(self.request, "Reset link send to your registered email")
        return super().form_valid(form)


# class PasswordResetDone(PasswordResetDoneView):
#     template_name = 'password/password_reset_done.html'
    # extra_context = {}

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'password/password_reset_confirm.html'
    success_url = reverse_lazy('home')
    # form_class
    # token_generator
    post_reset_login = True #Automatically logged in after resetting the password
    # post_reset_login_backend
    # extra_context

    def form_valid(self, form):
        messages.success(self.request, "Your password has been changed successfully.")
        return super().form_valid(form)


# class PasswordResetComplete(PasswordResetCompleteView):
#     template_name = 'password/password_reset_complete.html'
#     extra_context = {}


# class ChangePassword(PasswordChangeView):
#     template_name = 'password/password_change.html'
#
# class ChangePasswordDone(PasswordChangeDoneView):
#     template_name = 'password/password_change_done.html'
#
#
# class PasswordReset(PasswordResetView):
#     template_name = 'password/password_reset.html'
#
#
# class PasswordResetDone(PasswordResetDoneView):
#     template_name = 'password/password_reset_done.html'
#
#
# class PasswordResetConfirm(PasswordResetConfirmView):
#     template_name = 'password/password_reset_confirm.html'
#
#
# class PasswordResetComplete(PasswordResetCompleteView):
#     template_name = 'password/password_reset_complete.html'
