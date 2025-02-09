from rest_framework import serializers

class MarketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    description = serializers.CharField()
    net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)