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
        pass