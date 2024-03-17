from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),


    path('user/', UserViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='user_list'),
    path('user/<int:pk>/', UserViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),

    path('brand/', BrandViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='brand_list'),
    path('brand/<int:pk>/', BrandViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='brand_detail'),

    path('carusel/', CaruselPhotoViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='carusel_list'),
    path('carusel/<int:pk>/', CaruselPhotoViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='carusel_detail'),

    path('model/', ModelViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='model_list'),
    path('model/<int:pk>/', ModelViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='model_detail'),

    path('product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('product/<int:pk>/', ProductDetailViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('order/', OrderViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='order_list'),
    path('order/<int:pk>/', OrderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),

    path('favorite/', FavoriteViewSets.as_view({'get': 'list'}),
         name='favorite_list'),
    path('favorite/<int:pk>/', FavoriteViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorite_detail'),

    path('favorite_post/', FavoritePostViewSets.as_view({'post': 'create'}),
         name='favorite_post'),

    path('order/', OrderViewSets.as_view({'post': 'create'}),
         name='order_list'),
    path('order/<int:pk>/', OrderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),

    path('color/', ColorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='color_list'),
    path('color/<int:pk>/', ColorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='color_detail'),

    path('basket/', BasketViewSets.as_view({'get': 'list'}),
         name='basket_list'),
    path('basket/<int:pk>/', BasketViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='basket_detail'),

    path('basket_post/', BasketPostViewSets.as_view({'post': 'create'}),
         name='basket_post'),

    path('reviews/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='reviews_list'),
    path('reviews/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='reviews_detail'),

    path('news/', NewsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='news_list'),
    path('news/<int:pk>/', NewsViewSets.as_view({'get': 'retrieve'}),
         name='news_detail'),

    path('about/', AboutViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='about_list'),
    path('about/<int:pk>/', AboutViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='about_detail'),
]

#
# allouth
# filter
# search