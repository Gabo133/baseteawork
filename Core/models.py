from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.Usuario.username, filename])
def content_file_document(instance, filename):
    return '/'.join(['document', instance.Usuario.username, filename])

# class Camiones_Rigido(models.Model):
#     Categoria = models.CharField(max_length = 4,choices= (('Di','Diesel'),('Ga','Gasolina'),('Co','Combustible Alterno')), default = 'Di')
#     Tipo = models.CharField(max_length=2, choices=(('Tr','Tracto Camion'),('Un','Unitario')), default = 'Un')
#     Numero_Camiones = models.IntegerField(default = 0)
#     Kilometros_Promedio = models.IntegerField(default = 0)
#     Litros_Combustible = models.IntegerField(default = 0)
#     Promedio_Carga = models.IntegerField(default = 0)
#     Promedio_Ralenti = models.IntegerField(default = 0)
#     Dias_Operacion = models.IntegerField(default = 0)
#     Velocidad_Urbano = models.IntegerField(default = 0)
#     Velocidad_Interurbano = models.IntegerField(default = 0)
#     Proporcion_Urbano = models.IntegerField(default = 0)
#     Proporcion_Interurbano = models.IntegerField(default = 0)
#     Ano_Camion = models.IntegerField()
#     Masa = models.CharField(
#         max_length = 4,
#         choices = (
#             ('T1','< 7.5 Toneladas'),
#             ('T2','7.5 - 12 Toneladas'),
#             ('T3','12 - 14 Toneladas'),
#             ('T4','14 - 20 Toneladas'),
#             ('T5','20 - 26 Toneladas'),
#             ('T6','26 - 28 Toneladas'),
#             ('T7','28 - 32 Toneladas'),
#             ),
#         default='T1')
#     Tecnologia = models.CharField(
#         max_length = 4,
#         choices = (
#             ('Co','Convencional 805'),
#             ('E1','Euro I / EPA 91'),
#             ('E2','Euro II / EPA 94'),
#             ('E3','Euro III / EPA 98'),
#             ('E4','Euro IV EGR / EPA 2004'),
#             ('Gr','Euro V EGR / EPA 2007'),
#             ('Sc','Euro V SCR / EPA 2007'),
#             ('E6','Euro VI / EPA 2010'),),
#         default = 'E1')

#     Flota = models.ForeignKey(Flota, on_delete=models.CASCADE)
#     Estado = models.NullBooleanField(default=False)
#     Ano = models.IntegerField(default=datetime.date.today().year)
#     Dia = models.IntegerField(default=datetime.date.today().day)
#     Mes = models.IntegerField(default=datetime.date.today().month)
#     def get_kilometros_totales(self):
#         return (self.Kilometros_Promedio * self.Numero_Camiones)
        

class Persona(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Rut = models.CharField(max_length=20,null=True,blank=True)
    Telefono_C = models.CharField(max_length = 50,null=True,blank=True)
    Telefono_F = models.CharField(max_length = 50,null=True,blank=True)
    Cargo = models.CharField(max_length = 100,null=True,blank=True)
    Direccion = models.CharField(max_length = 400, null=True,blank=True)
    Comuna = models.CharField(max_length = 50, null=True,blank=True)
    Ciudad = models.CharField(max_length = 50,null=True,blank=True)
    Tipo = models.CharField(
        max_length = 2,
        choices=(
            ('EN', 'Encargado'),
            ('TR', 'Trabajador'),),
        null=True,blank=True)


class Situacion_Clinica(models.Model):
    Contacto_Numero = models.CharField(max_length = 50,null=True,blank=True)
    Detalle = models.CharField(max_length = 50,null=True,blank=True)
    Enfermedad = models.CharField(max_length = 50,null=True,blank=True)
    Contacto_Nombre = models.CharField(max_length = 50,null=True,blank=True)

class Horario(models.Model):
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(default=timezone.now)
    Mensaje = models.CharField(max_length = 50,null=True,blank=True)

class Grupo(models.Model):
    Nombre = models.CharField(max_length=100,null=True,blank=True)
    Encargado = models.ForeignKey(Persona, on_delete=models.CASCADE,related_name='Encargado')
    Trabajador = models.ForeignKey(Persona, on_delete=models.CASCADE,related_name='Trabajador')

# class Notificacion(models.Model):
#     Empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
#     Mensaje = models.TextField()
#     Estado = models.NullBooleanField(default=True)
#     Fecha = models.DateTimeField(default=timezone.now)
class Mensajeria(models.Model):
    Emisor = models.ForeignKey(Persona, on_delete=models.CASCADE,related_name='Emiso')
    Receptor = models.ForeignKey(Persona, on_delete=models.CASCADE,related_name='Receptor')
    Mensaje = models.TextField()
    Fecha = models.DateTimeField(default=timezone.now)

class Mensaje(models.Model):
    Informacion = models.TextField()
    Asunto = models.CharField(max_length=200,null=True,blank=True)
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(default=timezone.now)
    Estado = models.NullBooleanField(default=True)
class Receptor(models.Model):
    Mensaje = models.ForeignKey(Mensaje,on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Respuesta(models.Model):
    Mensaje = models.ForeignKey(Mensaje,on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Informacion = models.TextField()
    Fecha = models.DateTimeField(default=timezone.now)

class Respuesta_Respuesta(models.Model):
    Respuesta = models.ForeignKey(Respuesta,on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Informacion = models.TextField()
    Fecha= models.DateTimeField(default=timezone.now)
    