# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Product

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all().values()
#     return Response(products)

# @api_view(['GET'])
# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     return Response({
#         'name': product.name,
#         'price': product.price,
#         'description': product.description,
#         'image': product.image.url
#     })
# shop/views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
