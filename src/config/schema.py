from rest_framework import serializers


class StatusAndMessageSerializer(serializers.Serializer):
    status = serializers.BooleanField(
        help_text="true/false при false нужно смотреть message"
    )
    message = serializers.CharField(help_text="сообщение успеха/текст ошибки")
