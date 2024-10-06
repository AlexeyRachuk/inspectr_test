from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import OpenApiExample, extend_schema
from config.schema import StatusAndMessageSerializer
from users_app.models.users import Users
from users_app.serializers.users import UsersSerializer
import pandas as pd
from io import BytesIO


class UserListView(generics.ListAPIView):
    """
    Получение списка пользователей
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(
                age__icontains=search) | queryset.filter(email__icontains=search) | queryset.filter(
                tel__icontains=search)
        return queryset


class UserUploadView(APIView):
    """
    Загрузка файла и вывод в таблицу
    """
    parser_classes = (MultiPartParser, FormParser,)

    @extend_schema(
        request=None,
        responses={200: StatusAndMessageSerializer},
        examples=[
            OpenApiExample(
                name="Success",
                value={"status": "success", "message": "File uploaded successfully"},
                response_only=True,
            )
        ],
    )
    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file')
        if not file_obj:
            return Response({"status": "error", "message": "Не выбран файл"}, status=status.HTTP_400_BAD_REQUEST)

        if not file_obj.name:
            return Response({"status": "error", "message": "Нет имени файла"}, status=status.HTTP_400_BAD_REQUEST)

        # Читаем файл с помощью pandas
        try:
            if file_obj.name.endswith('.csv'):
                df = pd.read_csv(BytesIO(file_obj.read()))
            elif file_obj.name.endswith('.xlsx'):
                df = pd.read_excel(BytesIO(file_obj.read()))
            else:
                return Response({"status": "error", "message": "Некоректный формат"},
                                status=status.HTTP_400_BAD_REQUEST)

            # Сохраняем данные в модель Users
            for index, row in df.iterrows():
                Users.objects.create(
                    name=row['Имя'],
                    age=row['Возраст'],
                    email=row['Email'],
                    tel=row['Телефон']
                )

            return Response({"status": "success", "message": "Файл загружен"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
