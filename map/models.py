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


class Disease(models.Model):
    gho = models.CharField(max_length=20)
    year = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=6, null=True)
    country = models.CharField(max_length=5, null=True)
    numeric = models.IntegerField(null=True, blank=True)
    low = models.IntegerField(null=True, blank=True)
    high = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.gho


