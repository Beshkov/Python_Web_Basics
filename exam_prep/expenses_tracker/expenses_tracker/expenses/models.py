from django.db import models

# Create your models here.
class Expense(models.Model):
    title = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    image_url = models.URLField()
    price = models.FloatField()
