from django.urls import path

from business.apps import BusinessConfig
from business.views import (
    CompanyCreateAPIView,
    CompanyRetrieveAPIView,
    CompanyListAPIView,
    CompanyUpdateAPIView,
    CompanyDestroyAPIView,
)

app_name = BusinessConfig.name

urlpatterns = [
    path("company/create/", CompanyCreateAPIView.as_view(), name="company-create"),
    path("company/", CompanyListAPIView.as_view(), name="company-list"),
    path("company/<int:pk>/", CompanyRetrieveAPIView.as_view(), name="company-retrieve"),
    path("company/update/<int:pk>/", CompanyUpdateAPIView.as_view(), name="company-update"),
    path("company/delete/<int:pk>/", CompanyDestroyAPIView.as_view(), name="company-delete"),
]
