from rest_framework import viewsets
from .models import ProblemStatement, Tag
from .serializers import ProblemStatementSerializer, TagSerializer

class ProblemStatementViewSet(viewsets.ModelViewSet):
    queryset = ProblemStatement.objects.all()
    serializer_class = ProblemStatementSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
