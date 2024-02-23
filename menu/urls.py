from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
     # Garson çağrısı formu için URL
    path('call-garson/', views.call_garson, name='call_garson'),

    # Garson çağrısı listesi için URL
    path('garson-list/', views.garson_list, name='garson_list'),

    # Garson çağrısını silmek için URL
    path('delete-call/<int:call_id>/', views.delete_call, name='delete_call'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

