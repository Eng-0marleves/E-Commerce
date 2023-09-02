from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('Products.urls')),
    path('cart/',include('Carts.urls')),
    path('wishlist/',include('Wishlist.urls')),
    # path("__debug__/", include("debug_toolbar.urls")),
    path('', include('user_data.urls'))

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
