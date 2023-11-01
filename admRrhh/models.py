from typing import Any
from django.db import models

# Create your models here.
class Area(models.Model):
  nombre_are=models.CharField(max_length=50,verbose_name='Nombre')
  estado_are=models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return self.nombre_are
  
class Cargo(models.Model):
  nombre_carg=models.CharField(max_length=50,verbose_name='Nombre')
  estado_carg=models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return self.nombre_carg

class Documento(models.Model):
  nombre_doc=models.CharField(max_length=50,verbose_name='Nombre')
  estado_doc=models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return self.nombre_doc
  
class Estudio(models.Model):
  nombre_est=models.CharField(max_length=50,verbose_name='Nombre')
  estado_est=models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return self.nombre_est
  
class Profesion(models.Model):
  nombre_prof=models.CharField(max_length=50,verbose_name='Nombre')
  estado_prof=models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return self.nombre_prof
  
#////
class Persona(models.Model):
  nombre_per=models.CharField(max_length=15,verbose_name='Nombre')
  apellidoP_per=models.CharField(max_length=15,verbose_name='ApellidoP')
  apellidoM_per=models.CharField(max_length=15,verbose_name='ApellidoM')
  telf_per=models.CharField(max_length=15,verbose_name='Telefono')
  sexo_per=models.CharField(max_length=20,verbose_name='Tipo de sexo')
  numDoc_per=models.CharField(max_length=15,verbose_name='Numero de documento')
  exteDoc_per=models.CharField(max_length=6,verbose_name='Extension de documento')
  lugarNac_per=models.CharField(max_length=50,verbose_name='Lugar de nacimiento')
  sangre_per=models.CharField(max_length=10,verbose_name='Tipo de sangre')
  estCivil_per=models.CharField(max_length=20,verbose_name='Estado civil')
  hijos_per =models.PositiveIntegerField(default=0)
  fechIngre_per=models.DateField(verbose_name='Fecha ingreso')
  fechNac_per =models.DateField(verbose_name='Fecha nacimiento')
  vencDoc_per =models.DateField(verbose_name='Fecha vencimiento doc')
  licCond_per=models.CharField(max_length=2,verbose_name='Licencia de conducir')
  tipoLic_per=models.CharField(max_length=10,verbose_name='Tipo de Licencia')
  fechVenlic_per=models.DateField(verbose_name='Fecha vencimiento licencia')
  ctaBanc_per=models.CharField(max_length=20,verbose_name='Cuenta Bancaria')
  nua_per=models.CharField(max_length=20,verbose_name='Cuenta Nua')
  aseg_per=models.CharField(max_length=20,verbose_name='Cuenta asegurado')
  ctaAfp_per=models.CharField(max_length=20,verbose_name='Cuenta Afp')
  imagen =models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
  sueldo_per=models.FloatField(default=0)
  direccion_per=models.CharField(max_length=100,verbose_name='Direccion')
  nomFam1_per=models.CharField(max_length=40,verbose_name='Familiar1')
  celFam1_per=models.CharField(max_length=15,verbose_name='Cel_fam1')
  relcFam1_per=models.CharField(max_length=20,verbose_name='Relacion_fam1')
  nomFam2_per=models.CharField(max_length=40,verbose_name='Familiar2')
  celFam2_per=models.CharField(max_length=15,verbose_name='Cel_fam2')
  relcFam2_per=models.CharField(max_length=20,verbose_name='Relacion_fam2')
  documento_per=models.ForeignKey(Documento, null=True, blank=True, on_delete=models.CASCADE)
  estado_per=models.PositiveIntegerField(default=1)
class Personal(models.Model):
  persona_perl=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
  area_perl=models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)
  cargo_perl=models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)
  estudio_perl=models.ForeignKey(Estudio, null=True, blank=True, on_delete=models.CASCADE)
  profesion_perl=models.ForeignKey(Profesion, null=True, blank=True, on_delete=models.CASCADE)
  estado_perl=models.PositiveIntegerField(default=1)

    