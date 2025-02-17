from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)
        
    def update_rating(self):
        postsRating = self.post_set.all().aggregate(pr=Coalesce(Sum('rating'),0))['pr']
        commentsRating = self.authorUser.comment_set.all().aggregate(cr=Coalesce(Sum('rating'),0))['cr']
        postCommentsRating = self.post_set.all().aggregate(pcr=Coalesce(Sum('comment__rating'),0))['pcr']
        print(postsRating)
        print('-------------------')
        print(commentsRating)
        print('-------------------')
        print(postCommentsRating)
        self.ratingAuthor = postsRating * 3 + commentsRating + postCommentsRating
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField('Category', through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

class PostCategory(models.Model):
    postThrough = models.ForeignKey('Post', on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey('Category', on_delete=models.CASCADE)

class Comment(models.Model):
    commentPost = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.commentUser.username

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


