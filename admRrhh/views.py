from django.shortcuts import render, redirect
from django.db.models import Q
from . models import Area,Cargo,Documento,Estudio,Profesion,Persona,Personal
from django.contrib import messages


# Create your views here.
def base(resquest):
    return render(resquest,'index.html')

#AREA/////////////////////////////////////////////////////////
def areLista(resquest):
    areas =Area.objects.all()
    busqueda=resquest.GET.get("buscar")
    if busqueda:
        areas=Area.objects.filter(
            Q(nombre_are__icontains=busqueda)
        ).distinct()
    return render(resquest,'area/lista.html', { 'areas':areas})
def areCrear(resquest):
    return render(resquest,'area/crear.html')
def areGuardar(resquest):
    nombre = resquest.POST["nombre_are"]
    area=Area.objects.create(nombre_are=nombre.capitalize(),
                              estado_are= 1)
    messages.success(resquest, " SE REGISTRO CORRECTAMENTE ")
    return redirect('areLista')
def areEditar(resquest, id):
    codigo=Area.objects.get(id=id)
    return render(resquest,'area/editar.html', {'codigo':codigo } )
def areActualizar(resquest, id):
    nombre = resquest.POST["nombre_are"]
    area=Area.objects.get(id=id)
    area.nombre_are= nombre.capitalize()
    area.save()
    messages.success(resquest, " SE ACTUALIZO CORRECTAMENTE EL ARCHIVO ")
    return redirect('areLista')
def areEliminar(resquest, id):
    area=Area.objects.get(id=id)
    area.estado_are =0
    area.save()
    messages.success(resquest, " REGISTRO ELIMINADO ")
    return redirect('areLista')
#CARGO/////////////////////////////////////////////////////////
def cargLista(resquest):
    cargos =Cargo.objects.all()
    busqueda=resquest.GET.get("buscar")
    if busqueda:
        cargos=Cargo.objects.filter(
            Q(nombre_carg__icontains=busqueda)
        ).distinct()
    return render(resquest,'cargo/lista.html', { 'cargos':cargos})
def cargCrear(resquest):
    return render(resquest,'cargo/crear.html')
def cargGuardar(resquest):
    nombre = resquest.POST["nombre_carg"]
    cargo=Cargo.objects.create(nombre_carg=nombre.capitalize(),
                              estado_carg= 1)
    messages.success(resquest, " SE REGISTRO CORRECTAMENTE ")
    return redirect('cargLista')
def cargEditar(resquest, id):
    codigo=Cargo.objects.get(id=id)
    return render(resquest,'cargo/editar.html', {'codigo':codigo } )
def cargActualizar(resquest, id):
    nombre = resquest.POST["nombre_carg"]
    cargo=Cargo.objects.get(id=id)
    cargo.nombre_carg= nombre.capitalize()
    cargo.save()
    messages.success(resquest, " SE ACTUALIZO CORRECTAMENTE EL ARCHIVO ")
    return redirect('cargLista')
def cargEliminar(resquest, id):
    cargo=Cargo.objects.get(id=id)
    cargo.estado_carg =0
    cargo.save()
    messages.success(resquest, " REGISTRO ELIMINADO ")
    return redirect('cargLista')
#DOCUMENTO/////////////////////////////////////////////////////////
def docLista(resquest):
    documentos =Documento.objects.all()
    busqueda=resquest.GET.get("buscar")
    if busqueda:
        documentos=Documento.objects.filter(
            Q(nombre_doc__icontains=busqueda)
        ).distinct()
    return render(resquest,'documento/lista.html', { 'documentos':documentos})
def docCrear(resquest):
    return render(resquest,'documento/crear.html')
def docGuardar(resquest):
    nombre = resquest.POST["nombre_doc"]
    docum=Documento.objects.create(nombre_doc=nombre.capitalize(),
                              estado_doc= 1)
    messages.success(resquest, " SE REGISTRO CORRECTAMENTE ")
    return redirect('docLista')
def docEditar(resquest, id):
    codigo=Documento.objects.get(id=id)
    return render(resquest,'documento/editar.html', {'codigo':codigo } )
def docActualizar(resquest, id):
    nombre = resquest.POST["nombre_doc"]
    docum=Documento.objects.get(id=id)
    docum.nombre_doc= nombre.capitalize()
    docum.save()
    messages.success(resquest, " SE ACTUALIZO CORRECTAMENTE EL ARCHIVO ")
    return redirect('docLista')
def docEliminar(resquest, id):
    docum=Documento.objects.get(id=id)
    docum.estado_doc =0
    docum.save()
    messages.success(resquest, " REGISTRO ELIMINADO ")
    return redirect('docLista')
#ESTUDIO/////////////////////////////////////////////////////////
def estLista(resquest):
    estudios =Estudio.objects.all()
    busqueda=resquest.GET.get("buscar")
    if busqueda:
        estudios=Estudio.objects.filter(
            Q(nombre_est__icontains=busqueda)
        ).distinct()
    return render(resquest,'estudio/lista.html', { 'estudios':estudios})
def estCrear(resquest):
    return render(resquest,'estudio/crear.html')
def estGuardar(resquest):
    nombre = resquest.POST["nombre_est"]
    estudio=Estudio.objects.create(nombre_est=nombre.capitalize(),
                              estado_est= 1)
    messages.success(resquest, " SE REGISTRO CORRECTAMENTE ")
    return redirect('estLista')
def estEditar(resquest, id):
    codigo=Estudio.objects.get(id=id)
    return render(resquest,'estudio/editar.html', {'codigo':codigo } )
def estActualizar(resquest, id):
    nombre = resquest.POST["nombre_est"]
    estudio=Estudio.objects.get(id=id)
    estudio.nombre_est= nombre.capitalize()
    estudio.save()
    messages.success(resquest, " SE ACTUALIZO CORRECTAMENTE EL ARCHIVO ")
    return redirect('estLista')
def estEliminar(resquest, id):
    estudio=Estudio.objects.get(id=id)
    estudio.estado_est =0
    estudio.save()
    messages.success(resquest, " REGISTRO ELIMINADO ")
    return redirect('estLista')
#PROFESION/////////////////////////////////////////////////////////
def profLista(resquest):
    profesiones =Profesion.objects.all()
    busqueda=resquest.GET.get("buscar")
    if busqueda:
        profesiones=Profesion.objects.filter(
            Q(nombre_prof__icontains=busqueda)
        ).distinct()
    return render(resquest,'profesion/lista.html', { 'profesiones':profesiones})
def profCrear(resquest):
    return render(resquest,'profesion/crear.html')
def profGuardar(resquest):
    nombre = resquest.POST["nombre_prof"]
    profes = Profesion.objects.create(nombre_prof=nombre.capitalize(),
                              estado_prof= 1)
    messages.success(resquest, " SE REGISTRO CORRECTAMENTE ")
    return redirect('profLista')
def profEditar(resquest, id):
    codigo=Profesion.objects.get(id=id)
    return render(resquest,'profesion/editar.html', {'codigo':codigo } )
def profActualizar(resquest, id):
    nombre = resquest.POST["nombre_prof"]
    profes=Profesion.objects.get(id=id)
    profes.nombre_prof= nombre.capitalize()
    profes.save()
    messages.success(resquest, " SE ACTUALIZO CORRECTAMENTE EL ARCHIVO ")
    return redirect('profLista')
def profEliminar(resquest, id):
    profes=Profesion.objects.get(id=id)
    profes.estado_prof =0
    profes.save()
    messages.success(resquest, " REGISTRO ELIMINADO ")
    return redirect('profLista')
#PERSONA/////////////////////////////////////////////////////////
def perLista(resquest):
    personas =Persona.objects.all()
    busqueda=resquest.GET.get("buscar")
    if busqueda:
        personas=Persona.objects.filter(
            Q(nombre_per__icontains=busqueda)
        ).distinct()
    return render(resquest,'persona/lista.html', { 'personas':personas})
def perCrear(resquest):
    personas =Persona.objects.all()
    documentos =Documento.objects.all()
    return render(resquest,'persona/crear.html',{'personas':personas,'documentos':documentos})
def perGuardar(resquest):
    idocumento = resquest.POST["doc_per"]
    nombre = resquest.POST["nombre_per"]
    apellidoP = resquest.POST["apellidoP_per"]
    apellidoM = resquest.POST["apellidoM_per"]
    telf = resquest.POST["telf_per"]
    sexo = resquest.POST["sexo_per"]
    numDoc = resquest.POST["numDoc_per"]
    exteDoc = resquest.POST["exteDoc_per"]
    lugarNac = resquest.POST["lugarNac_per"]
    sangre = resquest.POST["sangre_per"]
    estCivil = resquest.POST["estCivil_per"]
    hijos = resquest.POST["hijos_per"]
    fechIngre = resquest.POST["fechIngre_per"]
    fechNac = resquest.POST["fechNac_per"]
    vencDoc = resquest.POST["vencDoc_per"]
    licCond = resquest.POST["licCond_per"]
    tipoLic = resquest.POST["tipoLic_per"]
    fechVenlic = resquest.POST["fechVenlic_per"]
    ctaBanc = resquest.POST["ctaBanc_per"]
    nua = resquest.POST["nua_per"]
    aseg = resquest.POST["aseg_per"]
    ctaAfp = resquest.POST["ctaAfp_per"]
    foto = resquest.FILES.get("foto_per")
    sueldo = resquest.POST["sueldo_per"]
    direccion = resquest.POST["direccion_per"]
    nomFam1 = resquest.POST["nomFam1_per"]
    celFam1 = resquest.POST["celFam1_per"]
    relcFam1 = resquest.POST["relcFam1_per"]
    nomFam2 = resquest.POST["nomFam2_per"]
    celFam2 = resquest.POST["celFam2_per"]
    relcFam2 = resquest.POST["relcFam2_per"]
    personas=Persona.objects.create(
    nombre_per=nombre.title(),
    apellidoP_per=apellidoP.capitalize(),
    apellidoM_per=apellidoM.capitalize(),
    telf_per=telf,
    sexo_per=sexo.capitalize(),
    numDoc_per=numDoc,
    exteDoc_per=exteDoc.upper(),
    lugarNac_per=lugarNac.capitalize(),
    sangre_per=sangre.upper(),
    estCivil_per=estCivil.capitalize(),
    hijos_per=hijos,
    fechIngre_per=fechIngre,
    fechNac_per=fechNac,
    vencDoc_per =vencDoc,
    licCond_per=licCond.capitalize(),
    tipoLic_per=tipoLic.upper(),
    fechVenlic_per=fechVenlic,
    ctaBanc_per=ctaBanc,
    nua_per=nua,
    aseg_per=aseg,
    ctaAfp_per=ctaAfp.capitalize(),
    imagen=foto,
    sueldo_per=sueldo,
    direccion_per=direccion.capitalize(),
    nomFam1_per=nomFam1.title(),
    celFam1_per=celFam1,
    relcFam1_per=relcFam1.capitalize(),
    nomFam2_per=nomFam2.title(),
    celFam2_per=celFam2,
    relcFam2_per=relcFam2.capitalize(),
    documento_per_id=idocumento)
    messages.success(resquest, " SE REGISTRO CORRECTAMENTE ")
    return redirect('perLista')
def perEditar(resquest, id):
    documentos=Documento.objects.all()
    codigo=Persona.objects.get(id=id)
    return render(resquest,'persona/editar.html', {'codigo':codigo, 'documentos':documentos})
def perActualizar(resquest, id):
    idocumento = resquest.POST["doc_per"]
    nombre = resquest.POST["nombre_per"]
    apellidoP = resquest.POST["apellidoP_per"]
    apellidoM = resquest.POST["apellidoM_per"]
    telf = resquest.POST["telf_per"]
    sexo = resquest.POST["sexo_per"]
    numDoc = resquest.POST["numDoc_per"]
    exteDoc = resquest.POST["exteDoc_per"]
    lugarNac = resquest.POST["lugarNac_per"]
    sangre = resquest.POST["sangre_per"]
    estCivil = resquest.POST["estCivil_per"]
    hijos = resquest.POST["hijos_per"]
    fechIngre = resquest.POST["fechIngre_per"]
    fechNac = resquest.POST["fechNac_per"]
    vencDoc = resquest.POST["vencDoc_per"]
    licCond = resquest.POST["licCond_per"]
    tipoLic = resquest.POST["tipoLic_per"]
    fechVenlic = resquest.POST["fechVenlic_per"]
    ctaBanc = resquest.POST["ctaBanc_per"]
    nua = resquest.POST["nua_per"]
    aseg = resquest.POST["aseg_per"]
    ctaAfp = resquest.POST["ctaAfp_per"]
    foto = resquest.FILES.get("foto_per")
    sueldo = resquest.POST["sueldo_per"]
    direccion = resquest.POST["direccion_per"]
    nomFam1 = resquest.POST["nomFam1_per"]
    celFam1 = resquest.POST["celFam1_per"]
    relcFam1 = resquest.POST["relcFam1_per"]
    nomFam2 = resquest.POST["nomFam2_per"]
    celFam2 = resquest.POST["celFam2_per"]
    relcFam2 = resquest.POST["relcFam2_per"]
    
    persona=Persona.objects.get(id=id)
    persona.nombre_per=nombre.title()
    persona.apellidoP_per=apellidoP.capitalize()
    persona.apellidoM_per=apellidoM.capitalize()
    persona.telf_per=telf
    persona.sexo_per=sexo.capitalize()
    persona.numDoc_per=numDoc
    persona.exteDoc_per=exteDoc.upper()
    persona.lugarNac_per=lugarNac.capitalize()
    persona.sangre_per=sangre.upper()
    persona.estCivil_per=estCivil.capitalize()
    persona.hijos_per=hijos
    persona.fechIngre_per=fechIngre
    persona.fechNac_per=fechNac
    persona.vencDoc_per =vencDoc
    persona.licCond_per=licCond.capitalize()
    persona.tipoLic_per=tipoLic.upper()
    persona.fechVenlic_per=fechVenlic
    persona.ctaBanc_per=ctaBanc
    persona.nua_per=nua
    persona.aseg_per=aseg
    persona.ctaAfp_per=ctaAfp.capitalize()
    persona.imagen=foto
    persona.sueldo_per=sueldo
    persona.direccion_per=direccion.capitalize()
    persona.nomFam1_per=nomFam1.title()
    persona.celFam1_per= celFam1
    persona.relcFam1_per=relcFam1.capitalize()
    persona.nomFam2_per=nomFam2.title()
    persona.celFam2_per=celFam2
    persona.relcFam2_per=relcFam2.capitalize()
    persona.documento_per_id=idocumento
    persona.save()
    messages.success(resquest, " SE ACTUALIZO CORRECTAMENTE EL ARCHIVO ")
    return redirect('perLista')
def perEliminar(resquest, id):
    persona=Persona.objects.get(id=id)
    persona.estado_per =0
    persona.save()
    messages.success(resquest, " REGISTRO ELIMINADO ")
    return redirect('perLista')
#PERSONAL/////////////////////////////////////////////////////////
def perlLista(resquest):
    personales =Personal.objects.all()
    personas =Persona.objects.all()
    areas =Area.objects.all()
    cargos =Cargo.objects.all()
    estudios =Estudio.objects.all()
    profesiones =Profesion.objects.all()
    busqueda=resquest.GET.get("buscar")
    if busqueda:
        personales=Personal.objects.filter(
            Q(nombre_perl__icontains=busqueda)
        ).distinct()
    return render(resquest,'personal/lista.html', { 'personales':personales,'personas':personas, 'areas':areas, 'cargos':cargos, 'estudios':estudios, 'profesiones':profesiones})
def perlCrear(resquest):
    personales =Personal.objects.all()
    personas =Persona.objects.all()
    areas =Area.objects.all()
    cargos =Cargo.objects.all()
    estudios =Estudio.objects.all()
    profesiones =Profesion.objects.all()
    return render(resquest,'personal/crear.html',{'personales':personales,'personas':personas,'areas':areas, 'cargos':cargos, 'estudios':estudios, 'profesiones':profesiones})
def perlGuardar(resquest):
    idpersona = resquest.POST["persona_perl"]
    idarea = resquest.POST["area_perl"]
    idcargo = resquest.POST["cargo_perl"]
    idestudio = resquest.POST["estudio_perl"]
    idprofesion = resquest.POST["profesion_perl"]
    personales=Personal.objects.create(
    persona_perl_id=idpersona,
    area_perl_id=idarea,
    cargo_perl_id=idcargo,
    estudio_perl_id=idestudio,
    profesion_perl_id=idprofesion)
    
    messages.success(resquest, " SE REGISTRO CORRECTAMENTE ")
    return redirect('perlLista')
def perlEditar(resquest, id):
    areas =Area.objects.all()
    cargos =Cargo.objects.all()
    estudios =Estudio.objects.all()
    profesiones =Profesion.objects.all()
    personas =Persona.objects.all()
    codigo=Personal.objects.get(id=id)
    return render(resquest,'personal/editar.html',{'codigo':codigo, 'areas':areas, 'personas':personas, 'cargos':cargos,'estudios':estudios, 'profesiones':profesiones } )

def perlActualizar(resquest, id):
    idpersona = resquest.POST["persona_perl"]
    idarea = resquest.POST["area_perl"]
    idcargo = resquest.POST["cargo_perl"]
    idestudio = resquest.POST["estudio_perl"]
    idprofesion = resquest.POST["profesion_perl"]
    personal=Personal.objects.get(id=id)
    personal.persona_perl_id=idpersona,
    personal.area_perl_id=idarea,
    personal.cargo_perl_id=idcargo,
    personal.estudio_perl_id=idestudio,
    personal.profesion_perl_id=idprofesion
    personal.save()
    messages.success(resquest, " SE ACTUALIZO CORRECTAMENTE EL ARCHIVO ")
    return redirect('perlLista')
def perlEliminar(resquest, id):
    personal=Personal.objects.get(id=id)
    personal.estado_perl =0
    personal.save()
    messages.success(resquest, " REGISTRO ELIMINADO ")
    return redirect('perlLista')