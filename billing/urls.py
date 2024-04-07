from django.urls import path

from .views import ProductListCreate,ProductRetriveUpdateDestroy, CustomerListCreate, CustomerRetrieveUpdateDestroy,TransactionListCreate, TransactionRetrieveUpdateDestroy, InvoiceListCreate, InvoiceRetrieveUpdateDestroy, CustomerDelete, ProductDelete, EmployeeTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', EmployeeTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', ProductListCreate.as_view(), name="products-create"),
    path('products/<int:pk>/', ProductRetriveUpdateDestroy.as_view(), name="product-detail"),
    path('products_del/<int:pk>/delete/', ProductDelete.as_view(), name='product-delete'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
    path('customers_del/<int:pk>/delete/', CustomerDelete.as_view(), name='customer-delete'),
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroy.as_view(), name='transaction-detail'),
    path('invoices/', InvoiceListCreate.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroy.as_view(), name='invoice-detail'),


]