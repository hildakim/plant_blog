from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Log(models.Model):
  log_title = models.CharField(max_length=200)
  nickname = models.CharField(max_length=100)
  upload_date = models.DateTimeField()
  log_body = models.TextField()
  image = models.ImageField(upload_to='log/', null=True, blank=True)
  image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(300, 200)])

  def __str__(self):
    return self.log_title 

  def summary(self):
    return self.log_body[:100]+'...'
