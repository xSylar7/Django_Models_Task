from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.
class Resturant (models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(default="", blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add = True)

