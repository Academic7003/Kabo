from django.urls import path, include
from portfolio.views import *

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioView.as_view(), name='main-portfolio' ),
    path('detail/<int:pk>', PortfolioDetail.as_view(), name='detail-portfolio'),
    path('update/<int:pk>', PortfolioUpdate.as_view(), name='update-portfolio'),
    path('create/', PortfolioCreate.as_view(), name='create-portfolio'),
    path('delete/<int:pk>', PortfolioDelete.as_view(), name='delete-portfolio'),
   

]


