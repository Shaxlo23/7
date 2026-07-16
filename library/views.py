from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .models import Library
from .serializers import LibrarySerializers

class LibraryListAPIView(ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class LibraryCreateAPIView(CreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class LibraryRetrieveAPIView(RetrieveAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class LibraryUpdateAPIView(UpdateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class LibraryDestroyAPIView(DestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class LibraryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class LibraryRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class LibraryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers