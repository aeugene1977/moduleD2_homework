from django.urls import path
from .views import PostsList, PostDetail

app_name = 'news'
urlpatterns = [
    path('',PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]