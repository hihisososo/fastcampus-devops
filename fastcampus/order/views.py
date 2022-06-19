from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Shop
from .serializers import ShopSerializer


@csrf_exempt
def shop(request):
  if request.method == 'GET':
    shop = Shop.objects.all()
    serializer = ShopSerializer(shop, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ShopSerializer(data=data)
    if (serializer.is_valid()):
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

