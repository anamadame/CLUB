from django.urls import path,include,re_path
from .views import *



urlpatterns = [

    path('accounts/', include('allauth.urls')),

    path('user/', UserViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='user_list'),
    path('user/<int:pk>/', UserViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),

    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),


    path('brand/', BrandViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='brand_list'),
    path('brand/<int:pk>/', BrandViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='brand_detail'),

    path('model/', ModelViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='model_list'),
    path('model/<int:pk>/', ModelViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='model_detail'),



    path('product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('product/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('harakter/', HaraktersViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='harakter_list'),
    path('harakter/<int:pk>/', HaraktersViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='haracter_detail'),

    path('storage/', StorageViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='storage_list'),
    path('storage/<int:pk>/', StorageViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='storage_detail'),

    path('carusel/', CaruselPhotoViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='carusel_list'),
    path('carusel/<int:pk>/', CaruselPhotoViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='carusel_detail'),


    path('reviews/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),
    path('reviews/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),


    path('ratings/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='ratings_list'),
    path('ratings/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='ratings_detail'),


    path('Order/', OrderViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='Order_list'),
    path('order_photos/<int:pk>/',
         OrderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),


    path('Color/', ColorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='Color_list'),
    path('order_photos/<int:pk>/',
         ColorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='color_detail'),




    path('product_photos/', ProductPhotoViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_photos_list'),
    path('product_photos/<int:pk>/', ProductPhotoViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_photos_detail'),


    path('favorites/', FavoriteViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='favorites_list'),
    path('favorites/<int:pk>/', FavoriteViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorites_detail'),


    path('baskets/', BasketViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='baskets_list'),
    path('baskets/<int:pk>/', BasketViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='baskets_detail'),
]