from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

class MyModel(models.Model):
    content = HTMLField()

    def get_absolute_url(self):
        return reverse ('home')