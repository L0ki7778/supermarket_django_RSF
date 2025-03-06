from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from .serializers import MarketSerializer, SellerSerializer, ProductSerializer
from market_app.models import Market, Seller, Product
from django.shortcuts import get_object_or_404
# from rest_framework.renderers import TemplateHTMLRenderer


class MarketView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

# @api_view(['GET', 'POST'])
# def market_view(request):
#     if request.method == 'GET':
#         markets = Market.objects.all()
#         serializer = MarketSerializer(markets, many=True, context={
#                                       'request': request}, fields={'id', 'name'})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MarketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class MarketDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# @api_view(['GET', 'DELETE', 'PUT'])
# def market_single_view(request, id):
#     if request.method == 'GET':
#         market = Market.objects.get(pk=id)
#         serializer = MarketSerializer(market, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         market = Market.objects.get(pk=id)
#         serializer = MarketSerializer(market)
#         market.delete()
#         return Response(f'Deleted: {serializer.data}')

#     if request.method == 'PUT':
#         market = Market.objects.get(pk=id)
#         serializer = MarketSerializer(market, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class RetrieveSellerView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SellersOfMarketListView(generics.ListCreateAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        market = Market.objects.get(pk=id)
        return market.sellers.all()

# //////////////////////////////////////////////////////////////    perform_create: is useful when applying additional logic before saving,
# //                                                        ////                    like getting the market-pk out of the url as reference for
# //                                                        ////                    the seller-creation
# //  def perform_create(self, serializer):                 ////    usecase here:   only useful if a single relation to a specific
# //        marked_id = self.kwargs.get('id')               ////                    market needs to be enforced, as it gets the id out of the
# //        market = Market.objects.get(pk = marked_id)     ////                    market-url
# //        serializer.save(markets = [market])             ////
# //                                                        ////
# //                                                        ////
# //////////////////////////////////////////////////////////////

# @api_view()
# def seller_single_view(request, pk):
#     if request.method == 'GET':
#         seller = Seller.objects.get(pk=pk)
#         serializer = SellerSerializer(seller)
#         return Response(serializer.data)


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


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self,request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data)
        else:
            return Response(product.errors)
