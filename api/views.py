from django.core import paginator
from django.http.response import HttpResponse
from django.views.generic.base import View
from .models import BankDetail
from .serializers import BankDetailSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .paginations import LimitOffsetPagination
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def homePage(request):
    return HttpResponse("Bank API")

@csrf_exempt
@api_view(['GET'])
def branchDetail(request):
    paginator = LimitOffsetPagination()
    reqobj = BankDetail.objects.filter(branch__contains=request.GET.get('q').upper()).order_by('ifsc')
    context = paginator.paginate_queryset(reqobj, request)
    sres = BankDetailSerializer(context, many=True)
    if(len(sres.data)==0): return Response({'message' : "Nothing Found!"}, status=status.HTTP_404_NOT_FOUND)
    return paginator.get_paginated_response({'branches' : sres.data})

@csrf_exempt
@api_view(['GET'])
def searchAllDetails(request):
    paginator = LimitOffsetPagination()
    reqobj_a = BankDetail.objects.filter(ifsc__contains=request.GET.get('q').upper())
    reqobj_b = BankDetail.objects.filter(branch__contains=request.GET.get('q').upper())
    reqobj_c = BankDetail.objects.filter(address__contains=request.GET.get('q').upper())
    reqobj_d = BankDetail.objects.filter(city__contains=request.GET.get('q').upper())
    reqobj_e = BankDetail.objects.filter(district__contains=request.GET.get('q').upper())
    reqobj_f = BankDetail.objects.filter(state__contains=request.GET.get('q').upper())
    reqobj_g = BankDetail.objects.filter(bank_name__contains=request.GET.get('q').upper())
    reqobj = (reqobj_a | reqobj_b | reqobj_c | reqobj_d | reqobj_e | reqobj_f | reqobj_g).distinct().order_by('ifsc')
    context = paginator.paginate_queryset(reqobj, request)
    sres = BankDetailSerializer(context, many=True)
    if(len(sres.data)==0): return Response({'message' : "Nothing Found!"}, status=status.HTTP_404_NOT_FOUND)
    return paginator.get_paginated_response({'branches' : sres.data})