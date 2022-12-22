from django.contrib import admin
from main.models import *

class PostImageAdmin(admin.StackedInline):
    model = IndexProductImage

@admin.register(IndexProduct)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = IndexProduct

@admin.register(IndexProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

