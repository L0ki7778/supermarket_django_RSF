from django.urls import path
from .views import market_view, market_single_view, seller_view, product_view, seller_single_view

urlpatterns = [
    path('market/', view=market_view),
    path('market/<int:id>', view=market_single_view, name='market-detail'),
    path('seller/', view=seller_view),
    path('seller/<int:pk>/', view=seller_single_view, name='seller_single'),
    path('products/', view=product_view),
    path('products/<int:id>', view=product_view),
]
