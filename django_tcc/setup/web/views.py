from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404

dict_item = {
    'key1': 'item 1',
    'key2': 'item 2',
}

@api_view(['GET'])
def show_item(request, item_id):
    return Response({'results': dict_item[item_id]})

    # try:
    #     return Response({'results': dict_item[item_id]})
    # except KeyError:
    #     raise Http404("Item not found")
