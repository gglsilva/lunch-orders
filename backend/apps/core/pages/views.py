from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from apps.order.models import Order
from django.conf import settings


# Create your views here.
def core_home(request):
    print(f'\n{settings.TEMPLATES}\n' )
    return render(request, 'core/index.html')


def dashboard_admin(request):

    template_name = "core/core.html"

    return render(request, template_name)


def fetch_return_all_orders_by_management(request):
   
    orders = Order.objects.all()

    data = [
        {
            'id': order.id,
            'data': order.created,
            'client': order.client.user.username,
            'products': order.get_product_for_order,
            'msg': order.return_note_with_string,
        } for order in orders
    ]

    return JsonResponse(data, safe=False)