from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile, Post


def home(request):

    posts = Post.objects.all().order_by(
        "-created_at"
    )

    return render(request, "home.html", {"posts": posts})

def login_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password") 
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")

def profile_page(request, username):
    user = get_object_or_404(
        User,
        username=username
    )

    profile = get_object_or_404(
        Profile,
        user=user
    )

    posts = Post.objects.filter(
        author=user
    )

    context = {
        "user": user,
        "profile": profile,
        "posts": posts,
    }
    return render(request, "profile.html", context)

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        Post.objects.create(
            author=request.user,
            title=title,
            content=content,
            image=image
        )
        return redirect("profile", request.user.username)
    return render(request, "create.html")


def detail_post(request, id):
    post = get_object_or_404(
        Post,
        id=id
    )
    return render(request, "detail.html", {"post":post})

@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        if request.FILES.get("image"):
            post.image = request.FILES.get("image")

        post.save()
        return redirect("detail", post.id)
    return render(request, "update.html", {"post":post})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == "POST":

        post.delete()
        return redirect("profile", request.user.username)
    
    return render(request, "delete.html", {"post":post})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            user.save()

            # create profile automatically
            Profile.objects.create(user=user)
            return redirect("login")
        else:
            return render(request, "register.html", {"error": "Password do not match"})

    return render(request, "register.html")
