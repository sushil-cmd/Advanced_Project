from django.urls import path
from .views import ItemDetailView,checkout,itemlist,product,HomeView


app_name ='core'

urlpatterns = [
    path('',HomeView.as_view(),name='item_list'),
    path('checkout/',checkout,name='checkout'),
    path('product/<slug>/',ItemDetailView.as_view(),name='product'),

]