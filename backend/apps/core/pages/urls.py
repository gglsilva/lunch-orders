from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.core_home, name='core_home'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('fetch/return/all/orders/', views.fetch_return_all_orders_by_management, name='fetch_return_all_orders_by_management'),
]