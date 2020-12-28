from news.models import News,Category
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    title=serializers.CharField(max_length=100)


class NewsSerializers(serializers.ModelSerializer):
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model=News
        fields=('title','content','created_at','update_at','photo','category')


    def create(self, validated_data):
        category_data=validated_data.pop('category')
        news_data=News.objects.create(**validated_data)
        Category.objects.create(news_data=news_data, **category_data)
        return  news_data
