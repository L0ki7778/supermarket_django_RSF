from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, SellerSerializer
from market_app.models import Market, Seller
# from rest_framework.renderers import TemplateHTMLRenderer


@api_view(['GET', 'POST'])
def market_view(request):
    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many=True,context={'request': request}, fields = {'id','name'})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def market_single_view(request, id):
    if request.method == 'GET':
        market = Market.objects.get(pk=id)
        serializer = MarketSerializer(market,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'DELETE':
        market = Market.objects.get(pk=id)
        serializer = MarketSerializer(market)
        market.delete()
        return Response(f'Deleted: {serializer.data}')

    if request.method == 'PUT':
        market = Market.objects.get(pk=id)
        serializer = MarketSerializer(market, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view()
def seller_single_view(request, pk):
    if request.method == 'GET':
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def seller_view(request):
    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
