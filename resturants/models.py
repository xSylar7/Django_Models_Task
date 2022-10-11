from datetime import datetime
from django.db import models

# Create your models here.
class Resturant (models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(default=datetime.now())

