from django.shortcuts import render, redirect
from ecom_store.models import Profile
from django.conf import settings
from ecom_store.forms import UserUpdateForm, ProfileUpdateForm


def user_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile, 'media_url': settings.MEDIA_URL})


def edit_user_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, 'profile/edit_profile.html', context)
