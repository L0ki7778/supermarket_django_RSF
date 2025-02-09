from django.urls import path
from .views import market_view, market_single_view

urlpatterns = [
    path('', view=market_view),
    path('<int:id>', view=market_single_view)
]
