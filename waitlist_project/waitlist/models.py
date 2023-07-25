from django.db import models

# Create your models here.
# tunr/models.py
class Services(models.Model):
    service = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Pictures(models.Model):
    title = models.CharField(max_length=100, default='none')
    photo_url = models.TextField()

    def __str__(self):
        return self.title