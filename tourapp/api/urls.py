from django.urls import path
from tourapp.api import views



app_name = "tourapp-api"

urlpatterns = [
   path('listcreate/',views.FavouriteListCreateAPIView.as_view(), name='listcreate'),
   path('updatedelete/<id>/',views.FavouriteAPIView.as_view(), name='updatedelete'),
   path('tourlist/',views.TourListView.as_view(), name='TourListView'),
   path('DestinationList/',views.DestinationListView.as_view(), name='DestinationListView'),
   path('DestinationRetrieve/<id>/',views.DestinationRetrieveView.as_view(), name='DestinationRetrieveView'),
   path('tour/<id>/',views.TourListDetailView.as_view(), name='TourListView'),
   path('BookMark/',views.BookMarkView.as_view(), name='BookMarkView'),
   path('CategoryTourView/',views.CategoryTourView.as_view(), name='CategoryTourView'),
   path('TypeTourView/',views.TypeTourView.as_view(), name='TypeTourView'),

   
]  
