from django.urls import path
from users_app.api.users import UserListView, UserUploadView
from users_app.views import index

urlpatterns = [
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/upload/', UserUploadView.as_view(), name='user-upload'),
    path('', index, name='index')
]
