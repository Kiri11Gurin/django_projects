from rest_framework import serializers
from .models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'price', 'amount']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be more than 0")
        return value

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be more than 0")
        return value
