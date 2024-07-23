from rest_framework import serializers

class UserBaseSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserSerializer(UserBaseSerializer):
    password = serializers.CharField(write_only=True)

class UserResponseSerializer(UserBaseSerializer):
    user_id = serializers.IntegerField()
    message = serializers.CharField()

class PurchaseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    item_name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    paid = serializers.BooleanField(default=False)

class PurchaseResponseSerializer(PurchaseSerializer):
    purchase_id = serializers.IntegerField()
    message = serializers.CharField()

class PaymentSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    purchase_id = serializers.IntegerField()

class PaymentResponseSerializer(PaymentSerializer):
    payment_id = serializers.IntegerField()
    message = serializers.CharField()
