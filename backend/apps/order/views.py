from apps.account.models import Profile
from apps.order.models import Order, OrderItem
from apps.product.models import Product, Category
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date, timedelta
from weasyprint import HTML
from django.core.files.storage import FileSystemStorage

import json


def action_fetch_create_order(request):
    
    if request.method != 'POST':
        return JsonResponse({'response': 'error', 'message': 'Método inválido. Apenas requisições POST são permitidas.'}, status=400)    
    
    data = json.loads(request.body)
    order_edit = data.get('order_number')
    produtos = data.get('produtos')
    cliente = data.get('cliente')
    mensagem = data.get('msg')
    profile = Profile.objects.get(user__username=cliente)

    if order_edit != None:
        
        order = Order.objects.get(id=int(order_edit))
        order.items.all().delete()
        order.note = mensagem
        order.save()
        
        for item in produtos:
            produto = Product.objects.get(id=int(item))
            OrderItem.objects.create(order=order,
                                    product=produto,
                                    )

        return JsonResponse({'response': 'success'})
    else:          

        order = Order.objects.create(client=profile, note=mensagem)
        for item in produtos:
            produto = Product.objects.get(id=int(item))
            OrderItem.objects.create(order=order,
                                    product=produto,
                                    )

        return JsonResponse({'response': 'success'})


def order_edit(request):
    
    user = request.user
    last_order = Order.objects.filter(client=user.profile).order_by('-id').first()

    categories = Category.objects.all()
    acompanhamento = Product.objects.filter(available=True, category=categories[0])
    opcao = Product.objects.filter(available=True, category=categories[1])
    profiles = Profile.objects.filter(is_active=True)

    order_itens = last_order.items.all()
    list_last_product_select = []

    order_number = last_order.id
    
    for item in order_itens:
        list_last_product_select.append(item.product.name)

    html = render_to_string(
        template_name='product/product_list.html',
        context={
            'opcoes': opcao,
            'acompanhamentos': acompanhamento,
            'profiles': profiles,
            'order_number': order_number,
            # 'last_order':list_last_product_select,
            'last_order':last_order,
            'note': last_order.note

        },  
        request=request
    )
    
    response = {
                    'data':html, 
                }
    
    return JsonResponse(response, safe=False)

def print_report_orders(request):
    today = date.today()
    orders = Order.objects.filter(created=date.today())
    html_string = render_to_string(
                            'order/pdf.html', 
                                {
                                    'orders': orders,
                                    'today': today
                                }
                            )

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/pedidos.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('pedidos.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="pedidos.pdf"'
    return response


def print_report_week(request):
    data_atual = date.today().date()

    # Criar uma lista para armazenar as datas
    datas_ultimos_5_dias = []

    # Loop para obter as datas dos últimos 5 dias
    for i in range(5):
        data = data_atual - timedelta(days=i)
        datas_ultimos_5_dias.append(data)

    # A lista `datas_ultimos_5_dias` agora contém as datas dos últimos 5 dias.
    print(datas_ultimos_5_dias)