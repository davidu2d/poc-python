from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    realeseYear = models.IntegerField()
    pages = models.IntegerField()
    createAt = models.DateField(auto_now_add=True)
