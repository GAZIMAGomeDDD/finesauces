from django.urls import path
from .views import order_create, invoice_pdf

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('admin/order/<int:order_id>/pdf/', invoice_pdf, name='invoice_pdf'),
]
