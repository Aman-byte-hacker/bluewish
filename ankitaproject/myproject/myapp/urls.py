from django.urls import path
from . import views
from myproject.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index,name="index"),
    path('products/',views.products,name="products"),
    path('arrivingproducts/',views.arrivingproducts,name="arrivingproducts"),
    path('see/<int:product_id>',views.see,name="see"),
    path('contact/',views.contact,name="contact"),
    path('contact',views.contact,name="contact")
    
] + static(MEDIA_URL,document_root=MEDIA_ROOT) 