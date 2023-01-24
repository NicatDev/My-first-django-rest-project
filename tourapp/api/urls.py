from django.urls import path
from tourapp.api import views



app_name = "tourapp-api"

urlpatterns = [
   path('listcreate/',views.FavouriteListCreateAPIView.as_view(), name='listcreate'),
   path('updatedelete/',views.FavouriteAPIView.as_view, name='updatedelete')
]  