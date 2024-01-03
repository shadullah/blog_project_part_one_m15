from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique = True, null=True, blank=True)
    # bio= models.TextField()

    def __str__(self):
        return self.name
