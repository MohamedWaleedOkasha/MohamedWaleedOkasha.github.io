# class About(models.Model):
#     content = models.TextField()

# class Contact(models.Model):
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)

# class Testimonial(models.Model):
#     name = models.CharField(max_length=100)
#     message = models.TextField()

# class BlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
