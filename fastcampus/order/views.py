from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Menu
from .models import Shop
from .serializers import MenuSerializer
from .serializers import ShopSerializer


@csrf_exempt
def shop(request):
  if request.method == 'GET':
    # shop = Shop.objects.all()
    # serializer = ShopSerializer(shop, many=True)
    # return JsonResponse(serializer.data, safe=False)

    shop = Shop.objects.all();
    return render(request, 'order/shop_list.html', {'shop_list': shop});

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ShopSerializer(data=data)
    if (serializer.is_valid()):
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def menu(request, shop):
  if request.method == 'GET':
    menu = Menu.objects.filter(shop=shop)
    # serializer = MenuSerializer(menu, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return render(request, 'order/menu_list.html',   {'menu_list': menu});

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = MenuSerializer(data=data)
    if (serializer.is_valid()):
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
