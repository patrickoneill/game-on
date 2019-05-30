from django.shortcuts import get_object_or_404
from merchandise.models import Merchandise

def basket_contents(request):
    
    basket = request.session.get('basket', {})
    
    basket_items = []
    total = 0
    merch_count = 0
    for id, quantity in basket.items():
        merch = get_object_or_404(Merchandise, pk=id)
        total += quantity * merch.price
        merch_count += quantity
        basket_items.append({'id':id, 'quantity': quantity, 'merch': merch})
    
    return {'basket_items': basket_items, 'total': total, 'merch_count':merch_count }