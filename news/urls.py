from django.urls import path
from .views import HomeNewsView,NewsByCategory,ViewDetail,CreateViews
    # index,
    # get_category, \
    # view_news,\
    # add_news,


urlpatterns=[
    # path('news/',index, name='home'),
    path('news/',HomeNewsView.as_view(), name='home'),
    # path('category/<int:category_id>/',get_category, name='category'),
    path('category/<int:pk>/',
         NewsByCategory.as_view(), name='category'),

    # path('news/<int:news_id>/', view_news , name='view_news'),

    path('news/<int:pk>/', ViewDetail.as_view(), name='view_news'),

    # path('news/add_news/', add_news, name='add_news'),

    path('news/add_news/', CreateViews.as_view(), name='add_news'),

]