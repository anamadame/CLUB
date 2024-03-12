from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Аналогично
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price', 'color']
    search_fields = ['name']


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()  # Исправление имени модели Review
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class CaruselPhotoViewSets(viewsets.ModelViewSet):
    queryset = CaruselPhoto.objects.all()
    serializer_class = CaruselPhotoSerializer
    permission_classes = [permissions.AllowAny]


class FavoriteViewSets(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()  # Аналогично
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.AllowAny]


class BasketViewSets(viewsets.ModelViewSet):
    queryset = Basket.objects.all()  # Аналогично
    serializer_class = BasketSerializer
    permission_classes = [permissions.AllowAny]


class BrandViewSets(viewsets.ModelViewSet):
    queryset = Brand.objects.all()  # Аналогично
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


class ModelViewSets(viewsets.ModelViewSet):
    queryset = Model.objects.all()  # Исправление имени модели Model
    serializer_class = ModelSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class ColorViewSets(viewsets.ModelViewSet):
    queryset = Color.objects.all()  # Аналоги чно
    serializer_class = ColorSerializer
    permission_classes = [permissions.AllowAny]


