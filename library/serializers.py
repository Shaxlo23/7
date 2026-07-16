from rest_framework import serializers
from .models import Library

class LibrarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ["title","created_at","author","description","genre","updated_at"]
        read_only_fields = ["id","created_at",'updated_at']