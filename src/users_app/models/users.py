from django.db import models


class Users(models.Model):
    """
    Модель пользователей
    """
    name = models.CharField(
        verbose_name="Имя",
        max_length=255,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст",
    )
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
    )
    tel = models.CharField(
        verbose_name="Телефон",
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "users_app_users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
