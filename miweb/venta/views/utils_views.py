from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from ..models import Producto


def get_product_price(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return JsonResponse({'precio': str(producto.precio)})