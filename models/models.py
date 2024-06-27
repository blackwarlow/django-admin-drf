from django.db import models


# Create your models here.
class TestModel(models.Model):
    field = models.CharField(
        verbose_name="field",
        max_length=100,
    )

    class Meta:
        verbose_name = "тестовая модель"
        verbose_name_plural = "тестовые модели"
