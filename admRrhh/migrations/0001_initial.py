# Generated by Django 4.2.6 on 2023-10-29 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_are', models.CharField(max_length=50, verbose_name='Nombre')),
                ('estado_are', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_carg', models.CharField(max_length=50, verbose_name='Nombre')),
                ('estado_carg', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_doc', models.CharField(max_length=50, verbose_name='Nombre')),
                ('estado_doc', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_est', models.CharField(max_length=50, verbose_name='Nombre')),
                ('estado_est', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prof', models.CharField(max_length=50, verbose_name='Nombre')),
                ('estado_prof', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_perl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admRrhh.area')),
                ('cargo_perl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admRrhh.cargo')),
                ('estudio_perl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admRrhh.estudio')),
                ('profesion_perl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admRrhh.profesion')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_per', models.CharField(max_length=15, verbose_name='Nombre')),
                ('apellidoP_per', models.CharField(max_length=15, verbose_name='ApellidoP')),
                ('apellidoM_per', models.CharField(max_length=15, verbose_name='ApellidoM')),
                ('telf_per', models.CharField(max_length=15, verbose_name='Telefono')),
                ('sexo_per', models.CharField(max_length=20, verbose_name='Tipo de sexo')),
                ('numDoc_per', models.CharField(max_length=15, verbose_name='Numero de documento')),
                ('exteDoc_per', models.CharField(max_length=6, verbose_name='Extension de documento')),
                ('lugarNac_per', models.CharField(max_length=50, verbose_name='Lugar de nacimiento')),
                ('sangre_per', models.CharField(max_length=10, verbose_name='Tipo de sangre')),
                ('estCivil_per', models.CharField(max_length=20, verbose_name='Estado civil')),
                ('hijos_per', models.PositiveIntegerField(default=0)),
                ('fechIngre_per', models.DateField(verbose_name='Fecha ingreso')),
                ('fechNac_per', models.DateField(verbose_name='Fecha nacimiento')),
                ('vencDoc_per', models.DateField(verbose_name='Fecha vencimiento doc')),
                ('licCond_per', models.CharField(max_length=2, verbose_name='Licencia de conducir')),
                ('tipoLic_per', models.CharField(max_length=10, verbose_name='Tipo de Licencia')),
                ('fechVenlic_per', models.DateField(verbose_name='Fecha vencimiento licencia')),
                ('ctaBanc_per', models.CharField(max_length=20, verbose_name='Cuenta Bancaria')),
                ('nua_per', models.CharField(max_length=20, verbose_name='Cuenta Nua')),
                ('aseg_per', models.CharField(max_length=20, verbose_name='Cuenta asegurado')),
                ('ctaAfp_per', models.CharField(max_length=20, verbose_name='Cuenta Afp')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('sueldo_per', models.FloatField(default=0)),
                ('direccion_per', models.CharField(max_length=100, verbose_name='Direccion')),
                ('nomFam1_per', models.CharField(max_length=40, verbose_name='Familiar1')),
                ('celFam1_per', models.CharField(max_length=15, verbose_name='Cel_fam1')),
                ('relcFam1_per', models.CharField(max_length=20, verbose_name='Relacion_fam1')),
                ('nomFam2_per', models.CharField(max_length=40, verbose_name='Familiar2')),
                ('celFam2_per', models.CharField(max_length=15, verbose_name='Cel_fam2')),
                ('relcFam2_per', models.CharField(max_length=20, verbose_name='Relacion_fam2')),
                ('estado_per', models.PositiveIntegerField(default=1)),
                ('documento_per', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admRrhh.documento')),
            ],
        ),
    ]
