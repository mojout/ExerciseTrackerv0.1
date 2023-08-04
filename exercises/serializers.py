from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

from .models import *
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['user', 'first_name', 'last_name', 'email', 'phone']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'position']


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['plan_type', 'discount_percent']


class ExerciseSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()
    plan = PlanSerializer()

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'execute_date', 'specialization', 'periodicity',
                  'patient', 'doctor', 'plan']