from django.urls import path
from tourapp.api import views



app_name = "tourapp-api"

urlpatterns = [
   path('listcreate/',views.FavouriteListCreateAPIView.as_view(), name='listcreate'),
   path('updatedelete/<id>/',views.FavouriteAPIView.as_view(), name='updatedelete'),
   path('tourlist/',views.TourListView.as_view(), name='TourListView'),
   path('tour/<id>/',views.TourListDetailView.as_view(), name='TourListView'),
]  