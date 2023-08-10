from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

from .models import *
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone']


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
    exercise_price_with_discount = serializers.SerializerMethodField()

    def get_exercise_price_with_discount(self, instance):
        return instance.exercise_price_with_discount

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'execute_date', 'specialization', 'periodicity',
                  'patient', 'doctor', 'plan', 'exercise_price_with_discount']
