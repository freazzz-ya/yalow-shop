from django.urls import path, include

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.orders_list, name='orders_list'),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'product/<int:pk>/',
        views.ProductDetailView.as_view(),
        name='profile_id',
    ),
    path('about/', views.about_view, name='about_view'),
    path('blog/', views.blog_view, name='blog_view'),
    path('shop/', views.ProductListView.as_view(), name='shop_view'),
    path('cart/', views.cart_view, name='cart_view'),
    path(
        'single_product/', views.single_product_view,
        name='single_produc_view'),
    path('contact/', views.contact_view, name='contact_view'),
]
