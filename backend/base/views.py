from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Vendor, PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer, PurchaseSerializer,PurchaseUpdateSerializer,HistoricalPerformanceSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


import random
import datetime
from datetime import timedelta
import json
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class PurchaseViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = PurchaseSerializer
    queryset = PurchaseOrder.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return PurchaseUpdateSerializer
        return PurchaseSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        vendor_id = self.request.query_params.get('vendor_id')    
        queryset = queryset.filter(vendor__id=vendor_id)    
        if queryset:  
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Please provide a valid userid as query parameter"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        context = {}
        item = self.get_object()
        item.delete()
        context["response"] = "purchase order deleted successfully"
        return Response(context, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        if purchase_order.acknowledgement_date is None:
            print(purchase_order.acknowledgement_date)
            current_datetime = datetime.datetime.now()
            purchase_order.acknowledgement_date = current_datetime + timedelta(days=3)
            purchase_order.save()

            return Response({'message': 'Purchase order acknowledged successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Purchase order already acknowledged'}, status=status.HTTP_200_OK)


class VendorViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:  
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "no vendor exist"}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        context = {}
        item = self.get_object()
        item.delete()
        context["response"] = "deletion successsful"
        return Response(context, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        purchase_order = self.get_object()
        if HistoricalPerformance.objects.filter(vendor=purchase_order).exists():   
            data=Vendor.objects.get(name=purchase_order)    
            serializer=VendorSerializer(data,many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No performance history for given vendor'}, status=status.HTTP_200_OK)



def home(request):
    return JsonResponse({'message': 'Setting up successfully completed'}, status=status.HTTP_200_OK)
