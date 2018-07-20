from django.db import models

# Create your models here.

class DiseaseType(models.Model):
    label = models.CharField(max_length=100)
    desc = models.TextField(blank=True)


class DiseaseInstance(models.Model):
    type = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    value = models.IntegerField(null=True)
    country = models.CharField(max_length=100)
    year = models.IntegerField()


