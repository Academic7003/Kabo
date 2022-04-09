from django.urls import path, include
from news.views import *


app_name = 'news'

urlpatterns = [
    path('', NewsView.as_view(), name='news-page'),
    path('detail/<int:pk>', NewsDetail.as_view(), name='detail'),
    path('update/<int:pk>', NewsUpdate.as_view(), name='update'),
    path('create/', NewsCreate.as_view(), name='create'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='delete'),
   

]
