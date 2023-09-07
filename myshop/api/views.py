from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import CartSerializer, ProductSerializer, CategorySerializer, ReviewSerializer
from shop.models import Cart, Product, Category, Review
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin


# Create your views here.
class ProductsViewSet(ModelViewSet):
    queryset = products = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter
]
    filterset_fields = ['category_id', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    pagination_class = PageNumberPagination
    # def get(self, request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)
    
# class ApiProduct(RetrieveUpdateDestroyAPIView):
#     queryset = products = Product.objects.all() 
#     serializer_class = ProductSerializer
    # def get(self, request, pk):
    #     product = get_object_or_404(Product, id=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    
    # def put(self, request, pk):
    #     product = get_object_or_404(Product, id=pk)
    #     serializer = ProductSerializer(product, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     product = get_object_or_404(Product, id=pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(ModelViewSet):
     queryset = products = Category.objects.all()
     serializer_class = CategorySerializer
    # def get(self, request):
    # def get(self, request):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

# class APICategory(RetrieveUpdateDestroyAPIView):
#     queryset = products = Product.objects.all() 
#     serializer_class = CategorySerializer
    # def get(self, request, pk):
    #     category = get_object_or_404(Category, id=pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)
    
    # def put(self, request, pk):
    #     category = get_object_or_404(Category, id=pk)
    #     serializer = CategorySerializer(category, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    # def delete(self, request, pk):
    #     category = get_object_or_404(Category, id=pk)
    #     category.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReviewViewSet(ModelViewSet):
     #queryset = Review.objects.all()
     serializer_class = ReviewSerializer

     def get_queryset(self):
          Review.objects.filter(product_id = self.kwargs['product_pk'])

     def get_serializer_context(self):
         return {'product_id': self.kwargs['product_pk']}
     
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
     queryset = Cart.objects.all()
     serializer_class = CartSerializer






        

