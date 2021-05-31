from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('chat', views.chat,name='chat'),
    path('chromeroom',views.chrome,name='chrome'),
    path('weatherroom', views.weather,name='weather')
]
