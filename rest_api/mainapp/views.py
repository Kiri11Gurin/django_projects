from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GoodSerializer
from .models import Good, Token
from uuid import uuid4


# Create your views here.
def get_token_view(request):
    if request.method == 'GET':
        token = Token()
        token.rand_token = uuid4()
        token.save()
        return JsonResponse({'token': token.rand_token})


@api_view(['GET'])
def goods_api(request):
    if 'token' in request.GET:
        user_token = request.GET['token']
        token_verification = Token.objects.filter(rand_token=user_token).first()
        if token_verification is not None:
            goods = Good.objects.all()
            serializer = GoodSerializer(goods, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse("Token is invalid", status=401)
    return HttpResponse("Token must be present", status=401)


@api_view(['POST'])
def new_good_view(request):
    if 'token' in request.GET:
        user_token = request.GET['token']
        token_verification = Token.objects.filter(rand_token=user_token).first()
        if token_verification is None:
            return HttpResponse("Token is invalid", status=401)
        if request.method == 'POST':
            form = GoodSerializer(data=request.data)
            if form.is_valid():  # автоматически вызываются validate_price и validate_amount
                form.save()
                return HttpResponse("<h3>Товар добавлен</h3>", status=201)
            else:
                return Response(form.errors, status=400)
    else:
        return HttpResponse("Token must be present", status=401)
