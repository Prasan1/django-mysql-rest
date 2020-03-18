
from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, PayloadViewSet

router = DefaultRouter()
router.register('service-request', ServiceViewSet, basename='service-api')
router.register('payload', PayloadViewSet, basename='payload-api')


urlpatterns = [
    re_path('', include(router.urls)),
]
