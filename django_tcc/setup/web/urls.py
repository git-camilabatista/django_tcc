from django.urls import path
from .views import (
    register_user, get_user,
    register_get_purchase, get_purchase,
    register_get_payment, get_payment,
    get_all_users, get_paid_purchases,
    get_total_purchases,
)

urlpatterns = [
    path('users', register_user, name='register_user'),
    path('users/<int:user_id>', get_user, name='get_user'),
    path('purchases', register_get_purchase, name='register_get_purchase'),
    path('purchases/<int:purchase_id>', get_purchase, name='get_purchase'),
    path('payments', register_get_payment, name='register_get_payment'),
    path('payments/<int:payment_id>', get_payment, name='get_payment'),
    path('admin/users', get_all_users, name='get_all_users'),
    path('admin/paid_purchases', get_paid_purchases, name='get_paid_purchases'),
    path('admin/total_purchases', get_total_purchases, name='get_total_purchases'),
]
