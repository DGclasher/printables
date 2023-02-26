from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from category import views as category_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('products/', views.product, name="products"),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('product/<int:pk>', views.product_details, name="product"),
    path('products/stickers/', views.stickers, name="stickers"),
    path('products/posters/', views.posters, name="posters"),
    path('products/t-shirs/', views.t_shirts, name="t_shirts"),
    path('products/customise/', views.customise, name="customise"),
    path('add_product/<int:pk>', category_views.add_to_cart, name="add_to_cart"),
    path('remove_product/<int:pk>', category_views.remove_from_cart, name="remove_from_cart")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

