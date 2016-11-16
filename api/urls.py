from django.conf.urls import url

from .views import OrderTotalView

urlpatterns = (
    url(r'^order-total$',
        view=OrderTotalView.as_view(),
        name='order-total-api'),
)
