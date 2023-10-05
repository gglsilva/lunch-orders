from django import template
from apps.order.models import Order
from datetime import date, timedelta

register = template.Library()

@register.simple_tag
def total_order(user):
    order_user = Order.objects.filter(client=user).count()
    return order_user

@register.simple_tag
def total_order_today(user):
    return Order.objects.filter(client=user, created=date.today()).count()

@register.simple_tag
def total_mean_order(user):
    return Order.objects.filter(client=user, created__gte=date.today() - timedelta(days=5)).count()