from django.urls import path
from .views import MarketView, MarketDetailView, seller_view, RetrieveSellerView,product_view,SellersOfMarketListView

urlpatterns = [
    path('market/', MarketView.as_view()),
    path('market/<int:id>', MarketDetailView.as_view(), name='market-detail'),
    path('market/<int:id>/sellers/', SellersOfMarketListView.as_view()),
    path('seller/', view=seller_view),
    path('seller/<int:pk>/', RetrieveSellerView.as_view(), name='seller_single'),
    path('product/', view=product_view)

]
