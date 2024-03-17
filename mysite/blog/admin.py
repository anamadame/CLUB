from django.contrib import admin
from .models import *


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [CharacteristicInline]
    list_display = ('name', 'model', 'price')

    def display_characteristics(self, obj):
        return ', '.join([f'{item.key}: {item.value}' for item in obj.characteristics.all()])

    display_characteristics.short_description = 'Characteristics'


admin.site.register(Product, ProductAdmin)
admin.site.register(Favorite)
admin.site.register(About)
admin.site.register(News)
admin.site.register(Photo)
admin.site.register(Order)
admin.site.register(Color)
admin.site.register(Basket)
admin.site.register(Reviews)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(CaruselPhoto)