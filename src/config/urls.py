from django.urls import path, include
from request_service import urls as reqeust_service_urls

urlpatterns = [
    path("api/", include(reqeust_service_urls))
]
