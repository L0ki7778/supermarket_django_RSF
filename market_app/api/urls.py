from django.urls import path
from .views import first_view

urlpatterns = [
    path('', view=first_view)
]
