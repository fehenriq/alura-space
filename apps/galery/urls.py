from django.urls import path
from apps.galery.views import \
    index, image, buscar, add_image, edit_image, delete_image, filtro

urlpatterns = [
    path("", index, name="index"),
    path("image/<int:foto_id>", image, name="image"),
    path("buscar", buscar, name="buscar"),
    path("add-image", add_image, name="add_image"),
    path("edit-image/<int:foto_id>", edit_image, name="edit_image"),
    path("delete-image/<int:foto_id>", delete_image, name="delete_image"),
    path("filtro/<str:categoria>", filtro, name="filtro"),
]
