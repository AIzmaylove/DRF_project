from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AutorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    serializer_class = AutorModelSerializer
    queryset = Author.objects.all()
