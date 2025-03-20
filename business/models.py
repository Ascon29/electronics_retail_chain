from django.db import models


class Company(models.Model):
    FACTORY = "0"
    RETAIL_CHAIN = "1"
    IP = "2"
    HIERARCHY_LEVELS = (
        (FACTORY, "0"),
        (RETAIL_CHAIN, "1"),
        (IP, "2"),
    )
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Название организации", help_text="Введите название организации"
    )

    email = models.EmailField(unique=True, verbose_name="Email адрес", help_text="Введите email")
    country = models.CharField(max_length=100, verbose_name="Страна", help_text="Введите страну")
    city = models.CharField(max_length=100, verbose_name="Город", help_text="Введите город")
    street = models.CharField(max_length=100, verbose_name="Улица", help_text="Введите улицу", blank=True, null=True)
    house_number = models.CharField(
        max_length=10, verbose_name="Номер дома", help_text="Введите номер дома", blank=True, null=True
    )
    hierarchy_level = models.CharField(
        choices=HIERARCHY_LEVELS, verbose_name="Уровень иерархии сети", help_text="Укажите уровень иерархии"
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Поставщик",
        help_text="Выберите поставщика",
        blank=True,
        null=True,
    )
    debt = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Задолженность перед поставщиком", blank=True, null=True
    )
    creation_time = models.DateTimeField(auto_now=True, verbose_name="Время создания")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название продукта", help_text="Введите название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель", help_text="Введите модель продукта")
    release_date = models.DateField(
        verbose_name="Дата выхода продукта на рынок",
        help_text="Введите дату выхода продукта на рынок",
        blank=True,
        null=True,
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
