from django.urls import path
from .views import PList, PDetail, create_p

urlpatterns = [path('p/', PList.as_view()),
               path('p/<int:pk>/', PDetail.as_view(), name='p_detail'),
               path('create/', create_p, name='p_create'),]


