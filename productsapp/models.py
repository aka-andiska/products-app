from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)