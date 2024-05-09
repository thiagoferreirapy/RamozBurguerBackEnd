from django.urls import path
from .views import ProductCreateListView, CategoryCreateListView, ProductListView, AdditionaListView, BagCreateListView


urlpatterns = [
    path('product/', ProductCreateListView.as_view(), name='products-create-list'),
    path('category/', CategoryCreateListView.as_view(), name='category-create-list'),
    path('products/<str:pk>/', ProductListView.as_view(), name='burguer-list'),
    path('additional/<str:pk>/', AdditionaListView.as_view(), name='additional-list'),
    path('bag/', BagCreateListView.as_view(), name='bag-create-list'),
] 
