from django.urls import path
from .views import market_view, market_single_view, seller_view, seller_single_view,product_view

urlpatterns = [
    path('market/', view=market_view),
    path('market/<int:id>', view=market_single_view, name='market-detail'),
    path('seller/', view=seller_view),
    path('seller/<int:pk>/', view=seller_single_view, name='seller_single'),
    path('product/', view=product_view)

]
