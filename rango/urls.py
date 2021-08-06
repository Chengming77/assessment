from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('sport/', views.sport, name='sport'),
    path('athlete/', views.athlete, name='athlete'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('collected_data/', views.collected_data, name='collected_data'),
    path('sport/', views.show_sport, name='sport'),
    path('athlete/', views.show_athlete, name='athlete'),
    path('like_sport/', views.like_sport, name='like_sport'),
    path('like_athlete/', views.like_athlete, name='like_athlete'),
]
