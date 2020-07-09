from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('cart/',views.cart,name="cart"),
    path('checkout-page/',views.checkout,name='checkout'),
    path('update-item/',views.UpdateItem,name='update-item'),
    path('process-order/',views.ProcessOrder,name='process-order')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)