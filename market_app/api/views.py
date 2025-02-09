from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer
from market_app.models import Market
# from rest_framework.renderers import TemplateHTMLRenderer


@api_view(['GET', 'POST'])
def market_view(request):
    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','DELETE'])
def market_single_view(request, id):
    if request.method == 'GET':
        market = Market.objects.get(pk=id)
        serializer = MarketSerializer(market)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        market = Market.objects.get(pk=id)
        serializer = MarketSerializer(market)
        market.delete()
        return Response(f'Deleted: {serializer.data}')
