from rest_framework import serializers
from .models import Products, Category, AdditionalFree, BagProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFree
        fields = "__all__"

class BagProductSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    type_meat = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BagProduct
        fields = "__all__"

    def get_name(self, obj):
        print(obj)
        nameproduct = obj.product_id
        if nameproduct:
            return nameproduct.name
        return f'Erro ao criar novo campo para name'
    
    def get_image(self, obj):
        print(obj)
        imageproduct = obj.product_id
        if imageproduct:
            return imageproduct.image.url
        return f'Erro ao criar novo campo para image'
    
    def get_type_meat(self, obj):
        print(obj)
        meat = obj.additional_meat
        if meat:
            return meat.name
        return f'Erro ao criar novo campo para type_meat'
    