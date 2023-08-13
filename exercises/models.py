from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.position}'


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('partial', 'Partial'),
        ('discount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])


class Exercise(models.Model):
    class Direction(models.TextChoices):
        PHYSIOTHERAPIST = 'PHY', 'Physiotherapist'
        PSYCHOLOGIST = 'PSY', 'Psychologist'

    title = models.CharField(max_length=255)
    execute_date = models.DateField(auto_now_add=True)
    specialization = models.CharField(max_length=3, choices=Direction.choices)
    periodicity = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    price = models.PositiveIntegerField(default=0)

