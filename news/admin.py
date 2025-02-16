from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

# class ProductOrderInline(admin.StackedInline):
#   model = ProductOrder
#   extra = 0
# class OrderAdmin(admin.ModelAdmin):
#   inlines = [ProductOrderInline,]
#   list_display = ('pk','total', 'time_out', 'take_away')
  
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
