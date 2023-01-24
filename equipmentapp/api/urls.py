from django.urls import path
from equipmentapp.api import views

app_name = "equipmentapp-api"

urlpatterns = [
   path("basket",views.BasketListView.as_view(), name="list"),
   path("basketadd/<slug>/",views.addbasketview.as_view(), name="list"),
   path("listc",views.ProductListView.as_view(), name='listc'),   
   path("create/",views.ProductCreateView.as_view(),name="create"),
]  
"""
urlpatterns = [
   path("list/", views.product_list_view, name="list"),
   path("cat/",views.category_list_view,name="cat"),
   path("detail/<int:id>",views.product_detail_view,name="detail"),
   path("listc/",views.ProductListView.as_view(), name='listc'),
   path("det/<slug>/",views.ProductRetrieveView.as_view(),name="det"),
   path("listi/",views.ImageView.as_view(),name='img'),
   path("create/",views.ProductCreateView.as_view(),name="create"),
   path("update/<slug>/", views.ProductUpdateView.as_view(), name="update"),
   path("delete/<slug>/", views.ProductDeleteView.as_view(), name="delete"),
   path("detailupde/<slug>/", views.ProductRetrieveUpdateDestroyView.as_view(), name="detail"),
]  """