from rest_framework import serializers

from users_app.models.users import Users


class UsersSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Пользователи
    """
    class Meta:
        model = Users
        fields = ['name', 'age', 'email', 'tel']
