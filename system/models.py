from django.db import models
from datetime import date

# Create your models here.
class Patients(models.Model):
    serial = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    bgroup = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    med = models.CharField(max_length=50)
    bill = models.CharField(max_length=50)
    payment = models.CharField(max_length=50)
    date1 = models.CharField(max_length=50)
    date2 = models.CharField(max_length=50, default=str(date.today()))


    class Meta:
        db_table = "patients"

    def __str__(self):
        return self.name