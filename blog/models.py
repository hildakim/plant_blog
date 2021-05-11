from django.db import models

# Create your models here.

class Blog(models.Model):
    post_title = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    upload_date = models.DateTimeField()
    post_body = models.TextField()
    
    def __str__(self):
        return self.post_title 

    def summary(self):
        return self.post_body[:100]+'...'