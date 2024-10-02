from django.urls import path
from App import views

app_name = 'App'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    # path('', views.App, name="App"),
]