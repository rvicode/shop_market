from django.urls import path
from . import views

app_name = 'list_for_shop'
urlpatterns = [
    path('shop', views.list_for_shop, name='list_for_shop'),
    path('cart', views.cart, name='cart'),
    path('check_our', views.check_out, name='check_out'),
    path('detail_shop/<int:pk>', views.detail_shop, name='detail_shop'),
    path('search', views.search_area, name='search'),
]
