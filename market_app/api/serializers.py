from rest_framework import serializers
from market_app.models import Market


def validate_no_X_letter(value):
    errors = []

    if 'X' in value:
        errors.append('no X allowed')
    if 'Y' in value:
        errors.append('no Y allowed')
    if errors:
        raise serializers.ValidationError(errors)

    return value


class MarketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(
        max_length=255, validators=[validate_no_X_letter])
    description = serializers.CharField()
    net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)

    def create(self, validated_data):
        return Market.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in ['name', 'location', 'description', 'net_worth']:
            setattr(instance, field, validated_data.get(
                field, getattr(instance, field)))
        # instance.name = validated_data.get('name', instance.name)
        # instance.location = validated_data.get('location', instance.location)
        # instance.description = validated_data.get('description', instance.description)
        # instance.net_worth = validated_data.get('net_worth', instance.net_worth)
        instance.save()
        return instance


class SellersDetailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    contact_info = serializers.CharField()
    # markets = serializers.ManyToManyField(Market, related_name="sellers")
