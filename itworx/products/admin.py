from django.contrib import admin

from .models import Product

from .models import user

admin.site.register(user)

admin.site.register(Product)