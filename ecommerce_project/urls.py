from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('shop.urls')),
    path('orders/', include('orders.urls')),
    path('', RedirectView.as_view(pattern_name='product_list', permanent=False)),
]
