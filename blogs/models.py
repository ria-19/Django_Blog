from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """ BlogPost"""
    topic = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.topic
