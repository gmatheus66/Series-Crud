from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.SerieDetailView.as_view(), name='detail'),
	path('edit/<int:pk>/', views.edit, name='edit'),
	path('serie/', views.serieview, name='serie'),
	path('delete/<int:pk>/', views.delete, name='delete'),


]