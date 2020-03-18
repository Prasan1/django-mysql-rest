
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.utils import json
from rest_framework.viewsets import GenericViewSet

from .models import Service
from .serializers import ServiceSerializer, PayloadSerializer


class ServiceViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Service Entry
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many

    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('active', 'requester', 'request_date',)


class PayloadViewSet(GenericViewSet,
                     CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     ListModelMixin,
                     ):
    serializer_class = PayloadSerializer
    queryset = Service.objects.all()
   
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('name',)














