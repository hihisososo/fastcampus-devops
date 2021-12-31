from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop,Menu,Order,Orderfood
from serializers import ShopSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


def shop(request):
    if request.method == 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='POST':
