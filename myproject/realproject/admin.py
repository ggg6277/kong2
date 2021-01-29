from django.contrib import admin
from .models import Test, Image, Product, Category, Post, Comment


class TestAdmin(admin.ModelAdmin):
    pass
class ImageAdmin(admin.ModelAdmin):
    pass
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Test, TestAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Product, ProductAdmin)
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)
