from rest_framework import generics
from .models import Products, Category, AdditionalFree, BagProduct
from .serializers import ProductSerializer, CategorySerializer, AdditionalSerializer, BagProductSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Products.objects.filter(category__name=pk).all()
        return queryset
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Nenhum produto encontrado"}, status=status.HTTP_404_NOT_FOUND)

class AdditionaListView(generics.ListAPIView):
    serializer_class = AdditionalSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = AdditionalFree.objects.filter(category_type=pk).all()
        return queryset
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Nenhum adicional encontrado"}, status=status.HTTP_404_NOT_FOUND)

class BagCreateListView(generics.ListCreateAPIView):
    queryset = BagProduct.objects.all()
    serializer_class = BagProductSerializer