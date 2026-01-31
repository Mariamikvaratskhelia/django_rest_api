from rest_framework import serializers
from .models import Items

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()

    created_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(required=False, default=True)
    quantity = serializers.IntegerField(required=False, default=0)
    category = serializers.CharField(required=False, allow_blank=True)

