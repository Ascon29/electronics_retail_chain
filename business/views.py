from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from business.models import Company
from business.permissions import UserIsActive
from business.serializers import CompanySerializer, CompanyUpdateSerializer


class CompanyCreateAPIView(CreateAPIView):
    """Контроллер создания компании"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [UserIsActive]


class CompanyListAPIView(ListAPIView):
    """Контроллер просмотра списка компаний"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [UserIsActive]
    filter_backends = [SearchFilter]
    search_fields = ["country"]


class CompanyRetrieveAPIView(RetrieveAPIView):
    """Контроллер просмотра информации о компании"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [UserIsActive]


class CompanyUpdateAPIView(UpdateAPIView):
    """Контроллер обновления информации о компании. Использует отдельный сериализатор, чтобы исключить возможность
    обновления поля 'задолженность перед поставщиком'"""

    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
    permission_classes = [UserIsActive]


class CompanyDestroyAPIView(DestroyAPIView):
    """Контроллер удаления компании"""

    queryset = Company.objects.all()
    permission_classes = [UserIsActive]
