from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Blog(models.Model):
    topic = models.CharField(max_length = 200)
    description = models.CharField(max_length = 10000)

    def __str__(self):
        return self.topic

class Entry(models.Model):
    titel = models.CharField(max_length = 200)
    content = models.CharField(max_length = 10000)
    pub_date = models.DateTimeField('date published')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.titel


