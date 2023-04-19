from django.urls import path
from . import views

app_name = "accounts-api"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.RegistrationView.as_view(), name="register"),
    path("check-post", views.CheckPost.as_view(), name="check_post"),
    path('UserPageView/<int:id>',views.UserPageView.as_view(),name='UserPageView'),
    path('ToursOfUserView/<int:id>',views.ToursOfUserView.as_view(),name='ToursOfUserView'),
    path('TourAddView/',views.TourAddView.as_view(),name='TourAddView'),
    path('MessagesOfTour/<int:id>',views.MessagesOfTour.as_view(),name='MessagesOfTour')
    
]