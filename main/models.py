from django.db import models


# Create your models here.


class lab_data:
    uid: int
    name: str
    age: int
    gender: str
    glucose: str
    sodium: str
    potassium: str
    co2: str
    cholesterol: str
    calcium: str
    phosphate: str
    iron: str
    date: str


class patient_dat:
    name: str
    uid: int


class reports(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, default="")
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=1, default="")
    glucose = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    sodium = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    potassium = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    co2 = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    calcium = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    phosphate = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    iron = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    date1 = models.CharField(max_length=25, default="")


class patient(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, default="")
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=1, default="")
    phn = models.BigIntegerField(default=0)


class employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=25, default="")
    doj = models.CharField(max_length=10, default="")
    salary = models.IntegerField(default=5000)
    d = models.IntegerField(default=1)


class lab_equipment(models.Model):
    eqp_name = models.CharField(max_length=50, default="")
    eqp_status = models.CharField(max_length=10, default='OK')
    eqp_condition = models.IntegerField(default=100)
