from django.urls import path
from . import views

urlpatterns = [

    
    path('create/', views.create, name="create"),
    path('view/<str:pk>', views.view, name="view"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),

]