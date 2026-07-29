from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("profile/<str:username>/", views.profile_page, name="profile"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("create/", views.create_post, name="create"),
    path("detail/<int:id>/", views.detail_post, name="detail"),
    path("update/<int:id>/", views.update_post, name="update"),
    path("delete/<int:id>/", views.delete_post, name="delete"),
    path("register/", views.register_view, name="register"),
]