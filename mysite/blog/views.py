from rest_framework import viewsets

from .models import *
from .serializers import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics




class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['brand', 'model', 'characteristics', 'price', 'color']
    search_fields = ['name']


class ProductDetailViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Исправление имени модели Review
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()  # Исправление имени модели Review
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class CaruselPhotoViewSets(viewsets.ModelViewSet):
    queryset = CaruselPhoto.objects.all()
    serializer_class = CaruselPhotoSerializer
    permission_classes = [permissions.AllowAny]


class FavoritePostViewSets(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoritePostSerializer
    permission_classes = [permissions.AllowAny]


class BasketPostViewSets(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketPostSerializer
    permission_classes = [permissions.AllowAny]



class FavoriteViewSets(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.AllowAny]  # Assuming you want to allow any user to create a favorite

    def create(self, request, *args, **kwargs):
        # Ensure that the product ID is provided in the request data
        if 'product' not in request.data:
            return Response({'product': ['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with creating the favorite
        return super().create(request, *args, **kwargs)


class BasketViewSets(viewsets.ModelViewSet):
    queryset = Basket.objects.all()  # Аналогично
    serializer_class = BasketSerializer
    permission_classes = [permissions.AllowAny]


class BrandViewSets(viewsets.ModelViewSet):
    queryset = Brand.objects.all()  # Аналогично
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand_name']


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


class ModelViewSets(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class ColorViewSets(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.AllowAny]


class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutViewSets(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]