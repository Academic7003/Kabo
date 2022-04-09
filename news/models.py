from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models
from django.urls import reverse
from uuid import uuid4




def upload_location(instance, filename):
    ext=filename.split('.')[-1]
    file_path= 'news_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)

    )
    return file_path


class NewsModel(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = upload_location, null=True, blank =True )
 
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('portfolio:detail', args=[str(self.id)])
    
    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url
