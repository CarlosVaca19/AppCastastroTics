from django.db import models

# Create your models here.
class funcionarios_gadma(models.Model):
    iden= models.CharField(verbose_name="Cedula", null=True, max_length=100) # ¿A que iglesia Pertenece?
    ent_nombre = models.CharField(verbose_name="Nombres", null=True, max_length=100) # Denominacion
    ent_apellido= models.CharField(verbose_name="Apellidos", null=True, max_length=200) # Direccion Iglesia, en el formulario considerar Calle, Canton, Provincia
    ent_ingreso = models.CharField(verbose_name="Fecha Ingreso") # ¿Eres mienbro?
    ent_salida = models.CharField(verbose_name="Fecha Salida",null=True)
    ent_cargo = models.CharField(verbose_name="Cargos ",null=True, max_length=200)
    ent_sexo = models.CharField(verbose_name="Sexo", null=True, max_length=2)
    dep_nombre = models.CharField(verbose_name="Departamento", null=True, max_length=70)
