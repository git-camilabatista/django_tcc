from django.urls import path
from .views import show_item

urlpatterns = [
    path('items/<str:item_id>', show_item, name='show_item'),
]