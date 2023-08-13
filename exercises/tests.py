import unittest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


class ExerciseApiTestCase(APITestCase):
    def setUp(self):
        plan = Plan.objects.create(plan_type="full", discount_percent=0)
        doctor = Doctor.objects.create(first_name="Николай", last_name="Борисов", position="Физиотерапевт")
        patient = Patient.objects.create(first_name="Николай", last_name="Морозов", email="m221out@yandex.ru",
                                         phone="89276884733")
        exercise = Exercise.objects.create(title="Комплекс упражнений для спины", execute_date="2023-08-03",
                                           specialization="PHY", periodicity=2, patient=patient, doctor=doctor,
                                           plan=plan)

        self.setup_data = [exercise]


class BaseTestCase(ExerciseApiTestCase):
    def setUp(self):
        super().setUp()

    def test_get_list(self):
        url = reverse('exercise-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


if __name__ == "__main__":
    unittest.main()
