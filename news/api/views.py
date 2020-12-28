from rest_framework.generics import ListCreateAPIView
from .serializers import NewsSerializers
from  news.models import News

class NewsApiView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers