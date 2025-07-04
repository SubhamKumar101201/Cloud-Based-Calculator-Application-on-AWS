from django.urls import path

from . import views

urlpatterns = [
    path('check', views.index, name='index'),
    path('store-result/', views.store_result, name='store-result'),
    path('get-results/', views.get_results, name='get-results')
]