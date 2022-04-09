from django.db import models
from ckeditor.fields import RichTextField


class Description(models.Model):

     title = models.CharField(max_length=150,unique=True)
     created_at=models.DateField()
     slug=models.CharField(max_length=150,unique=True)
     status=models.BooleanField(default=0)
     image = models.ImageField(upload_to='slider')
     detalis=RichTextField()

     def __str__(self):
          return self.title

