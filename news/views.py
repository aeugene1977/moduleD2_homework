# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostsList (ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')

# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news/new.html' # название шаблона будет product.html
    context_object_name = 'new' # название объекта