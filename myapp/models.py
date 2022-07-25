from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    rent=models.FloatField()
    emi=models.FloatField()
    tax=models.FloatField()
    other_exp=models.FloatField()
    monthly_exp=models.FloatField(default=0)
    monthly_inc=models.FloatField(default=0)
