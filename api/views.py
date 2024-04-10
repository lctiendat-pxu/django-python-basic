from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category ,Product
from .serializers import CategorySerializer,ProductSerializer
from django.http import Http404
import json
from django.shortcuts import get_object_or_404



class CategoryListCreateView (APIView):
    def get(self, format=json):
         categories = Category.objects.all()
         serializer = CategorySerializer(categories, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
     
    def post(self, request, format=None):
         serializer = CategorySerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class CategoryDetailView (APIView):
    def get_object(self, pk):
         try:
             return Category.objects.get(pk=pk)
         except Category.DoesNotExist:
             raise Http404
         except Category.MultipleObjectsReturned:
             raise Http404
        
    def get(self, request, pk, format=json):
         category = self.get_object(pk)
         serializer = CategorySerializer(category)
         return Response(serializer.data, status=status.HTTP_200_OK)
      
    def put(self, request, pk, format= json):
         category = self.get_object(pk)
         serializer = CategorySerializer(category, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=json):
         category = self.get_object(pk)
         category.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

class ProductListCreateView (APIView):
    def get(self, format=json):
         products = Product.objects.all()
         serializer = ProductSerializer(products, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
     
    def post(self, format=json):
         serializer = ProductSerializer(data=request.data)
         printf(request)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView (APIView):
    def get_object(self, pk):
         try:
             return Product.objects.get(pk=pk)
         except Product.DoesNotExist:
             raise Http404
         except Product.MultipleObjectsReturned:
             raise Http404
        
    def get(self, pk): 
        
        product = self.get_object(pk)
        serializer = CategorySerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format= json):
         product = self.get_object(pk)
         serializer = CategorySerializer(product, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    def delete(self, request, pk, format=json):
         product = self.get_object(pk)
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
     

class ProductsByCategory(APIView):
    def get(self, request, category_id, format=None):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)