from django.urls import path
from .views import  UserListCreateApiView

urlpatterns=[
    path('sign/',UserListCreateApiView.as_view())
]