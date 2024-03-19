from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class CaruselPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaruselPhoto
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Reviews.objects.all(), required=False, allow_null=True)
    product = serializers.SlugRelatedField(slug_field="name", queryset=Product.objects.all())

    class Meta:
        model = Reviews
        fields = ('user', 'text', 'stars', 'data', 'parent', 'product')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image',)

    def to_representation(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class ProductDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    color = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    characteristics = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    brand = serializers.SlugRelatedField(slug_field='brand_name', queryset=Brand.objects.all())
    model = serializers.SlugRelatedField(slug_field='name', queryset=Model.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def get_characteristics(self, obj):
        characteristics = obj.characteristics.all()
        characteristics_dict = {}
        for characteristic in characteristics:
            characteristics_dict[characteristic.key] = characteristic.value
        return characteristics_dict

    def get_reviews(self, obj):
        # Получаем все отзывы для данного продукта
        reviews = Reviews.objects.filter(product=obj)
        return self.get_recursive_reviews(reviews)

    def get_recursive_reviews(self, reviews):
        serialized_reviews = []
        for review in reviews:
            serialized_review = ReviewSerializer(review).data
            if review.parent:
                serialized_review['parent'] = self.get_recursive_reviews([review.parent])[0]
            else:
                serialized_review.pop('parent')  # Удаляем поле parent, если оно равно None
            serialized_reviews.append(serialized_review)
        return serialized_reviews


class BrandSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = Brand
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(slug_field='name', queryset=Color.objects.all(), many=True)
    first_photo = serializers.SerializerMethodField()  # Добавляем поле для первой фотографии
    brand = serializers.SlugRelatedField(slug_field='brand_name', queryset=Brand.objects.all())
    model = serializers.SlugRelatedField(slug_field='name', queryset=Model.objects.all())
    characteristics = serializers.SerializerMethodField()
    # brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())  # Добавляем поле для бренда
    # model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())

    class Meta:
        model = Product
        exclude = ('photos',)  # Исключаем ненужные поля
        # depth = 1  # Глубина вложенности, чтобы исключить связанные объекты

    def get_characteristics(self, obj):
        characteristics = obj.characteristics.all()
        characteristics_dict = {}
        for characteristic in characteristics:
            characteristics_dict[characteristic.key] = characteristic.value
        return characteristics_dict

    def get_first_photo(self, obj):
        first_photo = obj.photos.first()  # Получаем первую фотографию продукта
        if first_photo:  # Проверяем, что фотография существует
            return self.context['request'].build_absolute_uri(first_photo.image.url)
        return None


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)


    class Meta:
        model = Favorite
        fields = '__all__'


class FavoritePostSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Favorite
        fields = '__all__'
class ProductBasketSerializer(serializers.ModelSerializer):
    first_photo = serializers.SerializerMethodField()  # Добавляем поле для первой фотографии
    color = serializers.SlugRelatedField(slug_field='name', queryset=Color.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ('name', 'first_photo', 'stars', 'description', 'color')  # Ваши требуемые поля

    def get_first_photo(self, obj):
        first_photo = obj.photos.first()  # Получаем первую фотографию продукта
        if first_photo:  # Проверяем, что фотография существует
            return self.context['request'].build_absolute_uri(first_photo.image.url)
        return None


class BasketSerializer(serializers.ModelSerializer):
    product = ProductBasketSerializer(read_only=True)  # Используем наш сериализатор для поля продукта

    class Meta:
        model = Basket
        fields = '__all__'


class BasketPostSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Basket
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    products = BasketSerializer(many=True)  # Use ProductSerializer here

    class Meta:
        model = Order
        fields = '__all__'