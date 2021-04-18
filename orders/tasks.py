from celery import task
from django.core.mail import send_mail, EmailMessage
from .models import Order
from django.conf import settings
from io import BytesIO
from django.template.loader import render_to_string
import weasyprint


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'Your order was successfully created.\n' \
              f'Your order ID is {order.id}.'

    email = EmailMessage(
        subject,
        message,
        'eshop@finesauces.store',
        [order.email]
    )

    html = render_to_string('pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(str(settings.BASE_DIR) + '/listings/static/css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    email.attach(f'order_{order.id}.pdf',
        out.getvalue(),
        'application/pdf'
    )

    email.send()


@task
def status_change_notification(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n'\
              f'Status of your order {order.id} was changed to {order.status}'
    mail_sent = send_mail(
        subject,
        message,
        'eshop@finesauces.store',
        [order.email]
    )

    return mail_sent
