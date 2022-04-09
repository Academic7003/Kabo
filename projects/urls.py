from django.urls import path
from projects.views import *

app_name = 'projects'


urlpatterns = [
    path('', ProjectsView.as_view(), name = 'projects'),
    path('detail/<int:pk>', ProjectsDetail.as_view(), name='projects-detail'),
     path('update/<int:pk>', ProjectsUpdate.as_view(), name='projects-update'),
    path('create/', ProjectsCreate.as_view(), name='projects-create'),
    path('delete/<int:pk>', ProjectsDelete.as_view(), name='projects-delete'),



]
