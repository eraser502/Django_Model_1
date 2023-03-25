from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    contents = models.TextField()
    author = models.CharField(max_length=10)
    image = models.ImageField(upload_to="blog/%Y/%m/%d")

    def __str__(self):
        return self.title