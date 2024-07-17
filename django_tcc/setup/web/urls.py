from django.urls import path
from .views import UsersView, PurchasesView, PaymentsView, PaidPurchasesView

urlpatterns = [
    path('users', UsersView.as_view(), name='users'),
    path('users/<int:user_id>', UsersView.as_view(), name='get_users'),
    path('purchases', PurchasesView.as_view(), name='purchases'),
    path('purchases/<int:purchase_id>', PurchasesView.as_view(), name='get_purchases'),
    path('payments', PaymentsView.as_view(), name='payments'),
    path('payments/<int:payment_id>', PaymentsView.as_view(), name='get_payments'),
    path('paid_purchases', PaidPurchasesView.as_view(), name='paid_purchases'),
]