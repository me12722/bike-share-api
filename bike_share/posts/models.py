from __future__ import unicode_literals
from authentication.models import Account
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()
    image  = models.ImageField()
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)
    
