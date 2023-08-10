from django.db.models import F
from rest_framework.viewsets import ReadOnlyModelViewSet

from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer


class ExerciseView(ReadOnlyModelViewSet):
    queryset = Exercise.objects.all().prefetch_related('patient', 'doctor',
                                                       'plan').annotate(exercise_price_with_discount=F('price')
                                                                              - F('price')
                                                                              * F('plan__discount_percent') / 100.00)
    serializer_class = ExerciseSerializer
