from django.db import models

# Create your models here.

class Merchandise(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_length=6, decimal_place=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name