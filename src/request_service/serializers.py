from rest_framework.utils import json

from .models import Service
from rest_framework.fields import (
        CharField, IntegerField, DateField, JSONField
        )

from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    payload = serializers.JSONField()

    class Meta:
        order_by = ['id']
        model = Service
        fields = '__all__'


class PayloadSerializer(serializers.ModelSerializer):
    payload = serializers.JSONField()

    class Meta:
        model = Service
        fields = 'payload',




