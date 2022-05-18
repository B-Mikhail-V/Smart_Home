from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementInfoSerializer, SensorDetailSerializer, MeasurementSerializer


# Обновление данных о датчике
class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Список датчиков и добавление (создание) датчика
class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Занесение результатов измерений
class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# Полная информация о датчике с результатами измерений
class SensorDetailInfo(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

