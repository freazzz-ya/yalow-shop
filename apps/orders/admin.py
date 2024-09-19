from django.contrib import admin
from .models import Categories, SubCategories, Product

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Product)

# Register your models here.
