from django.urls import path
# from .views import UsersView, PurchasesView, PaymentsView, PaidPurchasesView

from .views import (
    register_user, get_user,
    register_purchase, get_purchase, get_all_purchases,
    register_payment, get_payment, get_all_payments,
    get_all_users, get_paid_purchases
)

urlpatterns = [
    path('users/', register_user, name='register_user'),
    path('users/<int:user_id>/', get_user, name='get_user'),
    path('purchases/', register_purchase, name='register_purchase'),
    path('purchases/<int:purchase_id>/', get_purchase, name='get_purchase'),
    path('all-purchases/', get_all_purchases, name='get_all_purchases'),
    path('payments/', register_payment, name='register_payment'),
    path('payments/<int:payment_id>/', get_payment, name='get_payment'),
    path('all-payments/', get_all_payments, name='get_all_payments'),
    path('admin/users/', get_all_users, name='get_all_users'),
    path('admin/paid_purchases/', get_paid_purchases, name='get_paid_purchases'),
]
