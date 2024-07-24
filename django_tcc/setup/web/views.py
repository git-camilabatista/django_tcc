from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (
    UserSerializer, UserResponseSerializer,
    PurchaseSerializer, PurchaseResponseSerializer,
    PaymentSerializer, PaymentResponseSerializer
)

users = {}
purchases = {}
payments = {}

def get_valid_user(user_id):
    user = users.get(user_id)
    if user:
        return user
    return None


# Users
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user_data = serializer.validated_data
        if any(u['email'] == user_data['email'] for u in users.values()):
            return Response({'detail': 'User already registered'}, status=status.HTTP_400_BAD_REQUEST)
        user_id = len(users) + 1
        users[user_id] = user_data
        return Response(UserResponseSerializer({'user_id': user_id, 'email': user_data['email'], 'message': 'User registered successfully'}).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request, user_id):
    user = get_valid_user(user_id)
    if user:
        return Response(UserResponseSerializer({'user_id': user_id, 'email': user['email'], 'message': 'User retrieved successfully'}).data)
    return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


# Purchases
@api_view(['POST'])
def register_purchase(request):
    serializer = PurchaseSerializer(data=request.data)
    if serializer.is_valid():
        purchase_data = serializer.validated_data
        if purchase_data['user_id'] not in users:
            return Response({'detail': 'Invalid or missing user_id'}, status=status.HTTP_400_BAD_REQUEST)
        purchase_id = len(purchases) + 1
        purchases[purchase_id] = purchase_data
        return Response(PurchaseResponseSerializer({'purchase_id': purchase_id, 'message': 'Purchase registered successfully', **purchase_data}).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_purchase(request, purchase_id):
    user_id = request.headers.get('X-User-Id')
    user = get_valid_user(int(user_id))
    if not user:
        return Response({'detail': 'Invalid user'}, status=status.HTTP_404_NOT_FOUND)
    purchase = purchases.get(purchase_id)
    if purchase and purchase['user_id'] == int(user_id):
        return Response(purchase)
    return Response({'detail': 'Purchase not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_purchases(request):
    user_id = request.headers.get('X-User-Id')
    user = get_valid_user(int(user_id))
    if not user:
        return Response({'detail': 'Invalid user'}, status=status.HTTP_404_NOT_FOUND)
    user_purchases = {pid: p for pid, p in purchases.items() if p['user_id'] == int(user_id)}
    if user_purchases:
        return Response(user_purchases)
    return Response({'detail': 'No purchases found'}, status=status.HTTP_404_NOT_FOUND)


# Payments
@api_view(['POST'])
def register_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        payment_data = serializer.validated_data
        purchase_id = payment_data['purchase_id']
        
        # Verificar se o purchase_id é válido
        if purchase_id not in purchases:
            return Response({'detail': 'Invalid or missing purchase_id'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verificar se já existe um pagamento registrado para essa compra
        if any(p['purchase_id'] == purchase_id for p in payments.values()):
            return Response({'detail': 'Payment already registered for this purchase'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Registrar o novo pagamento
        payment_id = len(payments) + 1
        payments[payment_id] = payment_data
        purchases[purchase_id]['paid'] = True
        
        return Response(PaymentResponseSerializer({
            'payment_id': payment_id,
            'message': 'Payment registered successfully',
            **payment_data
        }).data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_payment(request, payment_id):
    user_id = request.headers.get('X-User-Id')
    user = get_valid_user(int(user_id))
    if not user:
        return Response({'detail': 'Invalid user'}, status=status.HTTP_404_NOT_FOUND)
    payment = payments.get(payment_id)
    if payment and payment['user_id'] == int(user_id):
        return Response(payment)
    return Response({'detail': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_payments(request):
    user_id = request.headers.get('X-User-Id')
    user = get_valid_user(int(user_id))
    if not user:
        return Response({'detail': 'Invalid user'}, status=status.HTTP_404_NOT_FOUND)
    user_payments = {pid: p for pid, p in payments.items() if p['user_id'] == int(user_id)}
    if user_payments:
        return Response(user_payments)
    return Response({'detail': 'No payments found'}, status=status.HTTP_404_NOT_FOUND)


# Admin
@api_view(['GET'])
def get_all_users(request):
    return Response(users)


@api_view(['GET'])
def get_paid_purchases(request):
    paid_purchases_count = sum(1 for purchase in purchases.values() if purchase['paid'])
    return Response({'paid_purchases_count': paid_purchases_count})