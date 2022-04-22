from django.db import models

# Create your models here. 
class Article(models.Model):
    title = models.CharField(max_length=100) #CharField는 max_length가 필수!
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# article 1개(PK) -> comment N개(FK)
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self): # print(객체)
    #     return self.content + '광석'
