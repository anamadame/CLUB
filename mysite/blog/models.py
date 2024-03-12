from django.contrib.auth.models import User
from django.db import models
from .tel import *


class Brand(models.Model):
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="images/brand/", blank=True, null=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='product_photos/', verbose_name='фото продукта')




class Characteristic(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='characteristics')
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, default=1, related_name='model')
    name = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание')
    color = models.ManyToManyField(Color, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    warranty = models.IntegerField(null=True, blank=True)
    photos = models.ManyToManyField(Photo, blank=True, verbose_name='фото продукта')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                default=1, verbose_name="Оценка")

    def __str__(self):
        return self.name



    def __str__(self):
        return self.name



class CaruselPhoto(models.Model):
    photo = models.ImageField(upload_to="images/carusel/", blank=True, null=True)
    title = models.TextField(default="Default Title")

    def __str__(self):
        return self.title



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_favorite', default=1)
    product_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, default=1)
    count = models.PositiveIntegerField(verbose_name='количество товара', default=1)
    summ_products = models.IntegerField(verbose_name="общая сумма")

    def save(self, *args, **kwargs):
        # Calculate the total sum based on count and product price
        self.summ_products = self.count * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name

    def get_products_names(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Basket)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Save the Order instance first to generate an id
        super(Order, self).save(*args, **kwargs)
        notify_telegram_about_order(self)

    def __str__(self):
        return f'{self.user.username} - {self.total_amount}'

def notify_telegram_about_order(order):
        # Создаем сообщение для отправки в Telegram
        products = ', '.join([basket.product.name for basket in order.products.all()])
        message = f"Новый заказ!\nID заказа: {order.id}\nПользователь: {order.user.username}\n" \
                  f"Товары: {products}\n" \
                  f"Сумма заказа: {order.total_amount}\n"

        # Отправляем сообщение в Telegram
        bot.send_message(TELEGRAM_ID, message)  # Убедитесь, что 'bot' и 'TELEGRAM_ID' корректно определены


class Reviews(models.Model):
    """Отзывы"""
    user = models.ForeignKey(User, models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="продукт", on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                help_text="Rate the item with 0 to 6 stars.", verbose_name="Rating")

    def __str__(self):
        return f"{self.user.username} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"