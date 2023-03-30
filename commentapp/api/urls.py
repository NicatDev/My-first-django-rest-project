from django.urls import path
from commentapp.api import views

app_name = "commentapp-api"

urlpatterns = [
   path("create",views.CommentCreateAPIView.as_view(), name="create"),
   path("tccreate",views.TourCommentCreateAPIView.as_view(), name="tccreate"),
   path("pccreate",views.ProductCommentCreateAPIView.as_view(), name="pccreate"),
   path("comment/",views.CommentListAPIView.as_view(), name="comment"),
   path("delete/<id>/",views.CommentDeleteAPIView.as_view(), name="delete"),
   path("update/<id>/",views.CommentUpdateAPIView.as_view(), name="update"),
   path("blog/",views.BlogListAPIView.as_view(), name="blog"),
   path("blogdetail/<id>/",views.BlogDetailAPIView.as_view(), name="blogdetail"),

]  