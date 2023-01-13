from django.urls import path
from galery.views import index, image, buscar

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:foto_id>', image, name='image'),
    path('buscar', buscar, name="buscar")
]
