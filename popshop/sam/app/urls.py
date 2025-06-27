from django.urls import path
from .views import UserDetail, UserList, Mailgb, CreateUser

urlpatterns = [
    path('', Mailgb.as_view()),
    path('user/', UserList.as_view(), name="user"),
    path('jop/', UserList.as_view(), name="jop"),
    path("index/", CreateUser.as_view(), name='index')
]

