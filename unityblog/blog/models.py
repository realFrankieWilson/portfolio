""" models deals with database manipulations and how data are stored """
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
        Defines the attributes for the columns
        arttributes ->
            title:      The title of a particular post
            content:    The content of the post
            author:     The post creator(in relation to foreign key of the
                        post's author)
            created_at: Tracks date and time of when post was made
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Orders contents by date"""
        ordering = ('-created_at',)

    def __str__(self):
        """returns the post's title in a formarted string"""
        return self.title

class Comment(models.Model):
    """Comment class"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content