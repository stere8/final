from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('<int:pk>/', views.listing_detail, name='listing_detail'),
    path('new/', views.listing_create, name='listing_create'),
    path('<int:pk>/edit/', views.listing_update, name='listing_update'),
    path('<int:pk>/delete/', views.listing_delete, name='listing_delete'),
    path('search/', views.listing_search, name='listing_search'),
    path('success/', views.success, name='success'),
    path('/<int:pk>/reserve/', views.reserve_listing, name='reserve_listing'),

]
