from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("",views.home),
    path("contacts",views.contact),
    path("product",views.getProduct),
    path("checkout",views.checkout),
    path("cart/<product>",views.cart),
    
]
