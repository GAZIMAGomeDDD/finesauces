from django.urls import path
from .views import order_create, invoice_pdf, order_detail
from django.contrib.admin.views.decorators import staff_member_required
from finesauces_project.decorators import user_created_order

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('admin/order/<int:order_id>/pdf/', staff_member_required(invoice_pdf), name='invoice_pdf'),
    path('order/<int:order_id>/pdf/', user_created_order(invoice_pdf),
        name='customer_invoice_pdf'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
]
