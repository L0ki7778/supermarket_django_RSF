from django.urls import path, include
from .views import MarketView, MarketDetailView, seller_view, RetrieveSellerView, product_view, SellersOfMarketListView, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('market/', MarketView.as_view()),
    path('market/<int:id>', MarketDetailView.as_view(), name='market-detail'),
    path('market/<int:id>/sellers/', SellersOfMarketListView.as_view()),
    path('seller/', view=seller_view),
    path('seller/<int:pk>/', RetrieveSellerView.as_view(), name='seller_single'),
    # path('products/', view=product_view)

]
