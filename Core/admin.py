from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Persona)
admin.site.register(Situacion_Clinica)
admin.site.register(Horario)
admin.site.register(Grupo)
admin.site.register(Mensaje)
admin.site.register(Receptor)
admin.site.register(Respuesta)
admin.site.register(Respuesta_Respuesta)
admin.site.register(Mensajeria)