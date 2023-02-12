from django.urls import path
from equipmentapp.api import views

app_name = "equipmentapp-api"

urlpatterns = [
   path("basket/",views.BasketListView.as_view(), name="list"),
   path("basketadd/<id>/",views.addbasketview.as_view(), name="list"),
   path("listc/",views.ProductListView.as_view(), name='listc'),   
   path('detail/<id>/',views.ProductRetrieveView.as_view(), name='detail'),
#   path("create/",views.ProductCreateView.as_view(),name="create"),
]  

