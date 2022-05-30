from rest_framework import generics
from rest_framework.views import APIView

from . import models, serializer
from . import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookAPICreate(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookEditSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BookAPIList(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer


class BookAPIRetrieve(generics.RetrieveAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer


class BookAPIUpdate(generics.UpdateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookEditSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)


class BookAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookEditSerializer
    permission_classes = (permissions.IsAdminReadOnly,)

