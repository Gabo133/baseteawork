from django.urls import path, include
from Trabajador import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.Index, name="Index"),
    path('Horario/', views.Horario_Semana, name="Horario_Semana"),
    path('Mensajeria/', views.Mensajeria_Trabajador, name="Mensajeria_Trabajador"),
    path('Nueva_Tarea/', views.Nueva_Tarea, name="Nueva_Tarea"),
    path('Nuevo_Mensaje/', views.Nuevo_Mensaje, name="Nuevo_Mensaje"),
    path('Tareas/<int:dia>', views.Tareas, name="Tareas"),
    path('Ver_Companeros/', views.Ver_Companeros, name="Ver_Companeros"),
    path('Cuentionario/', views.Cuentionario, name="Cuentionario"),
#     path('Editar_Contacto/<int:pk>/', views.EditContact, name="EditContact"),
#     path('DelContact/<int:pk>/', views.DelContact, name="DelContact"),
#     path('Administar_Flota/', views.AdminFlota, name="AdminFlota"),
#     path('Agregar_Flota/', views.AgregarFlota, name="AgregarFlota"),
#     path('Editar_Flota/<int:pk>/', views.EditFlota, name="EditFlota"),
#     path('Eliminar_Flota/<int:pk>/', views.DelFlota, name="DelFlota"),
#     path('Camiones_Unitarios/<int:pk>/', views.CamionesUnitarios, name="CamionesUnitarios"),
#     path('TonUnitario/<int:pk>/', views.TonUnitario, name="TonUnitario"),
#     path('TractoCamiones/<int:pk>/', views.TractoCamiones, name="TractoCamiones"),
#     path('TonTractoCamion/<int:pk>/', views.TonTractoCamion, name="TonTractoCamion"),
#     path('Generar_Reporte/', views.GenerarReporte, name="GenerarReporte"),
#     path('Enviar_Informacion/', views.Validar, name="Validar"),
#     path('Fuentes_Informacion/', views.Fuentes_Informacion, name="Fuentes_Informacion"),
#     path('Cambiar_Contrasena/', views.Cambiar_Contrasena, name="Cambiar_Contrasena"),
#     path('Generar_Certificado/', views.Generar_Certificado, name="Generar_Certificado"),

#     path('Mensajeria_Empresa/', views_m.Mensajeria_Empresa, name="Mensajeria_Empresa"),
#     path('Foro_Empresa/<int:pk>/', views_m.Foro_Empresa, name="Foro_Empresa"),

#     path('CamionesUnitarios_edit/<int:pk_f>/<int:pk_c>', views.CamionesUnitarios_edit, name="CamionesUnitarios_edit"),
#     path('CamionesUnitarios_elim/<int:pk_f>/<int:pk_c>', views.CamionesUnitarios_elim, name="CamionesUnitarios_elim"),

#     path('CamionesTracto_elim/<int:pk_f>/<int:pk_c>', views.CamionesTracto_elim, name="CamionesTracto_elim"),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)