from django.urls import path
from equipmentapp.api import views

app_name = "equipmentapp-api"

urlpatterns = [
   path("basket/",views.BasketListView.as_view(), name="list"),
   path("basketadd/<slug>/",views.addbasketview.as_view(), name="list"),
   path("listc/",views.ProductListView.as_view(), name='listc'),   
   path('detail/<slug>/',views.ProductRetrieveView.as_view(), name='detail'),
#   path("create/",views.ProductCreateView.as_view(),name="create"),
]  

