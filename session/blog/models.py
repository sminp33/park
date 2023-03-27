from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    introduce = models.TextField()
    author = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title