from rest_framework import serializers

from business.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Сериализатр компании"""

    class Meta:
        model = Company
        fields = "__all__"


class CompanyUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления компании. Исключает поле 'debt(задолженность)',
    чтобы исключить возможность его изменения через API поля"""

    class Meta:
        model = Company
        fields = [
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "hierarchy_level",
            "supplier",
        ]
