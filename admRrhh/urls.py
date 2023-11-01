from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base, name='base' ),
    #/////AREA
    path('areLista',views.areLista, name='areLista'),
    path('areCrear',views.areCrear, name='areCrear'),
    path('areGuardar',views.areGuardar, name='areGuardar'),
    path('areEditar/<int:id>',views.areEditar, name='areEditar'),
    path('areActualizar/<int:id>',views.areActualizar, name='areActualizar'),
    path('areEliminar/<int:id>',views.areEliminar, name='areEliminar'),
    #/////CARGO
    path('cargLista',views.cargLista, name='cargLista'),
    path('cargCrear',views.cargCrear, name='cargCrear'),
    path('cargGuardar',views.cargGuardar, name='cargGuardar'),
    path('cargEditar/<int:id>',views.cargEditar, name='cargEditar'),
    path('cargActualizar/<int:id>',views.cargActualizar, name='cargActualizar'),
    path('cargEliminar/<int:id>',views.cargEliminar, name='cargEliminar'),
    #/////DOCUMENTO
    path('docLista',views.docLista, name='docLista'),
    path('docCrear',views.docCrear, name='docCrear'),
    path('docGuardar',views.docGuardar, name='docGuardar'),
    path('docEditar/<int:id>',views.docEditar, name='docEditar'),
    path('docActualizar/<int:id>',views.docActualizar, name='docActualizar'),
    path('docEliminar/<int:id>',views.docEliminar, name='docEliminar'),
    #/////ESTUDIO
    path('estLista',views.estLista, name='estLista'),
    path('estCrear',views.estCrear, name='estCrear'),
    path('estGuardar',views.estGuardar, name='estGuardar'),
    path('estEditar/<int:id>',views.estEditar, name='estEditar'),
    path('estActualizar/<int:id>',views.estActualizar, name='estActualizar'),
    path('estEliminar/<int:id>',views.estEliminar, name='estEliminar'),
    #/////PROFESION
    path('profLista',views.profLista, name='profLista'),
    path('profCrear',views.profCrear, name='profCrear'),
    path('profGuardar',views.profGuardar, name='profGuardar'),
    path('profEditar/<int:id>',views.profEditar, name='profEditar'),
    path('profActualizar/<int:id>',views.profActualizar, name='profActualizar'),
    path('profEliminar/<int:id>',views.profEliminar, name='profEliminar'),
    #/////PERSONA
    path('perLista',views.perLista, name='perLista'),
    path('perCrear',views.perCrear, name='perCrear'),
    path('perGuardar',views.perGuardar, name='perGuardar'),
    path('perEditar/<int:id>',views.perEditar, name='perEditar'),
    path('perActualizar/<int:id>',views.perActualizar, name='perActualizar'),
    path('perEliminar/<int:id>',views.perEliminar, name='perEliminar'),
     #/////PERSONAL
    path('perlLista',views.perlLista, name='perlLista'),
    path('perlCrear',views.perlCrear, name='perlCrear'),
    path('perlGuardar',views.perlGuardar, name='perlGuardar'),
    path('perlEditar/<int:id>',views.perlEditar, name='perlEditar'),
    path('perlActualizar/<int:id>',views.perlActualizar, name='perlActualizar'),
    path('pelrEliminar/<int:id>',views.perlEliminar, name='perlEliminar'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)