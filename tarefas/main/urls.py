from django.urls import path
from main import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:id>/', views.index, name='index'),
    path('', views.home, name='home'),
    path('view', views.view, name="view")
    
]