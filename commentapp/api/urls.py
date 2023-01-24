from django.urls import path
from commentapp.api import views

app_name = "commentapp-api"

urlpatterns = [
   path("create/",views.CommentCreateAPIView.as_view(), name="create"),
   path("list/",views.CommentListAPIView.as_view(), name="list"),
   path("delete/<slug>/",views.CommentDeleteAPIView.as_view(), name="delete"),
   path("update/<slug>/",views.CommentUpdateAPIView.as_view(), name="update"),

]  