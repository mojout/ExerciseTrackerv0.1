from rest_framework.viewsets import ReadOnlyModelViewSet

from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer


class ExerciseView(ReadOnlyModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
