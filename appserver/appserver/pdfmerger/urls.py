from django.urls import path
from . import views

urlpatterns = [
    path('', views.merger, name='index'),
    path('merge/', views.merge_pdfs, name='merge_pdfs'),
    ]