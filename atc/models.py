from django.db import models
from django.contrib.auth.models import User, Permission
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.

SIZES = [
    ('SMALL', 'Small'),
    ('MEDIUM', 'Medium'),
    ('LARGE', 'Large')
]


def isSizeValid(mySize: str, assginedsSize: str) -> bool:
    if mySize == 'SMALL':
        return True
    if mySize == 'MEDIUM' and assginedsSize not in ['MEDIUM', 'LARGE']:
        return False
    if mySize == 'LARGE' and assginedsSize != 'LARGE':
        return False
    return True


class Airline(ExportModelOperationsMixin("airline"), models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Airport(ExportModelOperationsMixin("airport"), models.Model):
    name = models.CharField(max_length=255, unique=True)
    x = models.FloatField()
    y = models.FloatField()
    airlines = models.ManyToManyField(Airline)

    def __str__(self):
        return self.name


class Gate(ExportModelOperationsMixin("gate"), models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    size = models.CharField(max_length=6, choices=SIZES, default='SMALL')
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier


class Runway(ExportModelOperationsMixin("runway"), models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    size = models.CharField(max_length=6, choices=SIZES, default='SMALL')
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier


class Plane(ExportModelOperationsMixin("plane"), models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    size = models.CharField(max_length=6,choices=SIZES,default='SMALL')
    currentPassengerCount = models.IntegerField(null=True)
    maxPassengerCount = models.IntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    gate = models.ForeignKey(Gate, on_delete=models.SET_NULL, blank=True, null=True)
    runway = models.ForeignKey(Runway, on_delete=models.SET_NULL, blank=True, null=True)
    take_off_airport = models.ForeignKey(Airport, related_name="take_off_airport", on_delete=models.SET_NULL, null=True)
    land_airport = models.ForeignKey(Airport, related_name="landing_airport", on_delete=models.SET_NULL, null=True)
    heading = models.FloatField(null=True)
    speed = models.FloatField(null=True)
    take_off_time = models.DateTimeField(null=True)
    landing_time = models.DateTimeField(null=True)
    arrive_at_gate_time = models.DateTimeField(null=True)
    arrive_at_runway_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.identifier
