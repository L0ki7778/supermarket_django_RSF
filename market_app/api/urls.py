from django.urls import path
from .views import market_view

urlpatterns = [
    path('', view=market_view)
]
