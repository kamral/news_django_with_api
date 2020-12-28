from django.urls import path
from .views import NewsApiView


urlpatterns=[
    path('',NewsApiView.as_view())
]