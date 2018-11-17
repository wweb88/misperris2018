from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from mascota.views import index, mascota_new, mascota_edit, mascota_delete, mascota_adoptar

urlpatterns = [
    url(r'^$', index.as_view(), name='index'),
    url(r'^nuevo$', mascota_new.as_view(), name='mascota_crear'),
    url(r'^editar/(?P<pk>\d+)/$', mascota_edit.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', mascota_delete.as_view(), name='mascota_eliminar'),
    url(r'^adoptar/(?P<pk>\d+)/$', login_required(mascota_adoptar.as_view()), name='mascota_adoptar'),
]