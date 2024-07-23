from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Dados em dicionários
users = {}
purchases = {}
payments = {}

class UsersView(APIView):
    def post(self, request):
        user_id = len(users) + 1
        user_data = request.data
        users[user_id] = user_data
        return Response(
            {
                "message": "User registered successfully", 
                "user_id": user_id
            }, 
            status=status.HTTP_201_CREATED
        )
    
    def get(self, request, user_id):
        user = users.get(user_id)
        if user:
            return Response(user, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class PurchasesView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id or user_id not in users:
            return Response(
                {"message": "Invalid or missing user_id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        purchase_id = len(purchases) + 1
        purchase_data = request.data
        purchases[purchase_id] = purchase_data
        return Response(
            {
                "message": "Purchase registered successfully", 
                "purchase_id": purchase_id
            }, 
            status=status.HTTP_201_CREATED
        )
    
    def get(self, request, purchase_id):
        purchase = purchases.get(purchase_id)
        if purchase is not None:
            return Response(purchase, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Purchase not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class PaymentsView(APIView):
    def post(self, request):
        purchase_id = request.data.get('purchase_id')
        if not purchase_id or purchase_id not in purchases:
            return Response(
                {"message": "Invalid or missing purchase_id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        payment_id = len(payments) + 1
        payment_data = request.data
        payments[payment_id] = payment_data
        purchases[purchase_id]['paid'] = True  # Marca a compra como paga
        return Response(
            {
                "message": "Payment registered successfully", 
                "payment_id": payment_id
            }, 
            status=status.HTTP_201_CREATED
        )
    
    def get(self, request, payment_id):
        payment = payments.get(payment_id)
        if payment is not None:
            return Response(payment, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Payment not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        

class PaidPurchasesView(APIView):
    def get(self, request):
        paid_purchases_count = sum(1 for purchase in purchases.values() if purchase.get('paid'))
        return Response(
            {"paid_purchases_count": paid_purchases_count},
            status=status.HTTP_200_OK
        )
    