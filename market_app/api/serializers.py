from rest_framework import serializers
from market_app.models import Market, Seller, Product


def validate_no_X_letter(instance, value):
    errors = []

    if 'X' in value:
        errors.append('no X allowed')
    if 'Y' in value:
        errors.append('no Y allowed')
    if errors:
        raise serializers.ValidationError(errors)

    return value


# class MarketSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # location = serializers.CharField(
    #     max_length=255)
    # description = serializers.CharField()
    # net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)

    # def create(self, validated_data):
    #     return Market.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     for field in ['name', 'location', 'description', 'net_worth']:
    #         setattr(instance, field, validated_data.get(
    #             field, getattr(instance, field)))
    #     # instance.name = validated_data.get('name', instance.name)
    #     # instance.location = validated_data.get('location', instance.location)
    #     # instance.description = validated_data.get('description', instance.description)
    #     # instance.net_worth = validated_data.get('net_worth', instance.net_worth)
    #     instance.save()
    #     return instance


class MarketSerializer(serializers.ModelSerializer):
    
    sellers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Market
        fields = '__all__'
        
        
    
class MarketHyperlinkedSerializer(MarketSerializer,serializers.HyperlinkedModelSerializer):
    # sellers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Market
        fields=['url']
        extra_kwargs = {
            'url':{
                'lookup_field':'id',
            }
        }


class SellerSerializer(serializers.ModelSerializer):
    market_names = serializers.SerializerMethodField()
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, source="markets")

    class Meta:
        model = Seller
        fields = '__all__'

    def get_market_names(self, instance):
        return instance.markets.values_list('name', flat=True)


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, write_only=True, source="markets")

    class Meta:
        model = Seller
        fields = '__all__'


# class SellersDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     contact_info = serializers.CharField()
#     markets = MarketSerializer(many=True, read_only=True, default=[])
#     # markets = serializers.StringRelatedField(many = True)


# class SellerCreateSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     contact_info = serializers.CharField()
#     markets = serializers.ListField(
#         child=serializers.IntegerField(), write_only=True)

#     def validate_markets(self, market_pk):
#         markets = Market.objects.filter(id__in=market_pk)
#         # len(markets) differs if a pk is provided, which is not availabe within db
#         # example: no market_pk "3"--> len(market_pg) is __gt the list of markets
#         if len(markets) != len(market_pk):
#             raise serializers.ValidationError(
#                 f"pk dismatch {market_pk} {len(markets)} {len(market_pk)}")
#         return market_pk

    # def create(self, validated_data):
    #     market_ids = validated_data.pop('markets')
    #     seller = Seller.objects.create(**validated_data)
    #     markets = Market.objects.filter(id__in=market_ids)
    #     seller.markets.set(markets)
    #     return seller


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    market = serializers.PrimaryKeyRelatedField(queryset=Market.objects.all())
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        for field in ["name", "description", "price", "market", "seller"]:
            setattr(instance, field, validated_data.get(
                field, getattr(instance, field)))
        instance.save()
        return instance
