from django.contrib import admin

# Register your models here.
from Balancing.models import *


class PostImageAdmin(admin.StackedInline):
    model = BalancingProductImage

@admin.register(BalancingProduct)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = BalancingProduct

@admin.register(BalancingProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass