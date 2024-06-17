# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),  # Use the custom logout view
    path('search/', views.account_search, name='account_search'),
    path('', views.accounts_list, name='accounts_list'),  # List of accounts
    path('<int:pk>/', views.account_detail, name='account_detail'),
]