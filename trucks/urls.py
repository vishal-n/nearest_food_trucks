from django.urls import path, register_converter
from .views import NearestTrucksView
from . import converters

register_converter(converters.FloatUrlParameterConverter, 'float')

app_name = "trucks"

urlpatterns = [
    path('nearest-trucks/', NearestTrucksView.as_view(), name="nearest_trucks")
]
