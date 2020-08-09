from django.db import models

# Create your models here.
class PostMainPage(models.Model):
    textMainPage = models.TextField()

    def __str__(self):
        return str(self.textMainPage)

class PhotoModel(models.Model):
    photo = models.ImageField(upload_to='image/', null=True, blank=True)
