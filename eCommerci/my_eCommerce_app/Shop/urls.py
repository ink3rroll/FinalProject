from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('sellers/', views.sellers, name='sellers'),
    path('sellers/details/<int:id>', views.seller_details, name='seller_details'),
    path('buyers/', views.buyers, name='buyers'),
    path('buyers/details/<int:id>', views.buyer_details, name='buyer_details'),
    path('products/', views.products, name='products'),
    path('products/details/<int:id>', views.product_details, name='product_details'),
    path('receipts/', views.receipts, name='receipts'),
    path('receipts/details/<int:id>', views.receipt_details, name='receipt_details'),
]