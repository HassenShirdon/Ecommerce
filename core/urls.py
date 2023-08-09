from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about', views.about_us, name='about'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('item/<int:pk>/', views.itemDetailView.as_view(), name='itemDetailView'),
    # URLs for Cart
    path('cart/<int:cart_id>/', views.cart_detail, name='cart_detail'),
    # URLs for Orders
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('search/', views.search_results, name='search_results'),
]
