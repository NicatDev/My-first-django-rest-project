from django.urls import path
from . import views

app_name = "accounts-api"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.RegistrationView.as_view(), name="register"),
<<<<<<< HEAD
    path("check-post", views.CheckPost.as_view(), name="check_post")
=======
>>>>>>> my-back-up
]