import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class OrderTotalView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderTotalView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            order_data = json.loads(request.body.decode("utf-8"))
            total = order_data.get('items_total')
            options = order_data.get('options', None)
            if options:
                for option in options:
                    total += option.get('price')

            return JsonResponse({'grand_total': total})
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=500)
        except Exception:
            return JsonResponse({'message': 'Something is wrong with request'}, status=500)
