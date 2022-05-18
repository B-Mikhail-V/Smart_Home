from django.contrib import admin
from django.urls import path

from .views import SensorUpdate, SensorListView, MeasurementCreate, SensorDetailInfo


urlpatterns = [
    path('sensor/<pk>/', SensorUpdate.as_view()),
    path('sensor_list/', SensorListView.as_view()),
    path('measure/', MeasurementCreate.as_view()),
    path('sensor_info/<pk>/', SensorDetailInfo.as_view()),
]
