from django.contrib import admin

from users_app.models.users import Users


@admin.register(Users)
class GuitarAdmin(admin.ModelAdmin):
    """
    Модель для админки
    """
    pass
