from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'




class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image',)

class ProductSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    brand = serializers.SlugRelatedField(slug_field="name", read_only=True)
    model = serializers.SlugRelatedField(slug_field="name", read_only=True)
    color = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'




class CaruselPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaruselPhoto
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


