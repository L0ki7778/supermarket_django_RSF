from django.urls import path
from .views import market_view, market_single_view,seller_view,product_view

urlpatterns = [
    path('market/', view=market_view),
    path('market/<int:id>', view=market_single_view),
    path('seller/', view=seller_view),
    path('products/', view=product_view),
]
