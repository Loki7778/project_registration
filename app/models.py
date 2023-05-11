from django.db import models

# Create your models here.
from django.core import validators

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(5)])


    def __str__(self):
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(5)])
    url=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name

