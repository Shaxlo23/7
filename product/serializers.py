from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title","created_at","price","description","updated_at","created_date"]
        read_only_fields = ["created_at",'id']