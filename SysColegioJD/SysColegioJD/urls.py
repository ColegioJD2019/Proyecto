"""SysColegioJD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from JuanDiegoSys.views import alumnosListado, alumnoInsertar, alumnoDetalle, alumnoActualizar, alumnoEliminar
from JuanDiegoSys.views import nivelListado, nivelInsertar, nivelDetalle, nivelActualizar, nivelEliminar
from JuanDiegoSys.views import carreraListado, carreraInsertar, carreraDetalle, carreraActualizar, carreraEliminar
from JuanDiegoSys.views import cargoListado, cargoInsertar, cargoDetalle, cargoActualizar, cargoEliminar
from JuanDiegoSys.views import personalListado, personalInsertar, personalDetalle, personalActualizar, personalEliminar
from JuanDiegoSys.views import gradoListado, gradoInsertar, gradoDetalle, gradoActualizar, gradoEliminar
from JuanDiegoSys.views import carrera_gradoListado, carrera_gradoInsertar, carrera_gradoDetalle, carrera_gradoActualizar, carrera_gradoEliminar
from JuanDiegoSys.views import cursoListado, cursoInsertar, cursoDetalle, cursoActualizar, cursoEliminar
from JuanDiegoSys.views import grado_cursoListado, grado_cursoInsertar, grado_cursoDetalle, grado_cursoActualizar, grado_cursoEliminar
from JuanDiegoSys.views import tutorListado, tutorInsertar, tutorDetalle, tutorActualizar, tutorEliminar
from JuanDiegoSys.views import estudiante_cursoListado, estudiante_cursoInsertar, estudiante_cursoDetalle, estudiante_cursoActualizar, estudiante_cursoEliminar
from JuanDiegoSys.views import notasListado, notasInsertar, notasDetalle, notasActualizar, notasEliminar
from JuanDiegoSys.views import colegiaturaListado, colegiaturaInsertar, colegiaturaDetalle, colegiaturaActualizar, colegiaturaEliminar
from django.views.generic.base import TemplateView
from JuanDiegoSys.views import AcercaView, homeNivelesEduView, cargosPersonalView, tutoresEstudiantesView, asignacionesView
from JuanDiegoSys import views

from datetime import datetime
import django.contrib.auth.views
import JuanDiegoSys.forms

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_view, name = 'login_view'),
    url(r'^accounts/login', views.login_view, name = 'login_view'),
    url(r'^home$', views.home, name = 'home'),
    url(r'^logout$', views.logout_view, name = 'logout_view'),
    url(r'^acerca$', AcercaView.as_view(), name='acerca'),
    path('home_niveles_edu/', homeNivelesEduView.as_view(), name='home_niveles_edu'),
    path('home_cargos_personal/', cargosPersonalView.as_view(), name='home_cargos_personal'),
    path('home_tutores_alumnos/', tutoresEstudiantesView.as_view(), name='home_tutores_alumnos'),
    path('home_asignaciones/', asignacionesView.as_view(), name='home_asignaciones'),
    path('', TemplateView.as_view(template_name='main.html'), name='principal'),
    # Urls para todo lo relacionado a cargos educativos
    path('cargos/', cargoListado.as_view(template_name = "Cargos/Cargos.html"), name='list_cargo'),
    path('cargos/insert_cargo', cargoInsertar.as_view(template_name = "Cargos/insertar_cargo.html"), name='ins_cargo'),
    path('cargos/detalle_cargo/<int:pk>', cargoDetalle.as_view(template_name = "Cargos/detalles_cargo.html"), name='det_cargo'),
    path('cargos/editar_cargo/<int:pk>', cargoActualizar.as_view(template_name = "Cargos/actualizar_cargo.html"), name='actu_cargo'),
    path('cargos/eliminar_cargo/<int:pk>', alumnoEliminar.as_view(), name='elim_estudiante'),
    # Urls para todo lo relacionado al personal del centro educativo
    path('personal_edu/', personalListado.as_view(template_name = "Personal/personal.html"), name='list_personal'),
    path('personal_edu/insert_personal', personalInsertar.as_view(template_name = "Personal/personal_insertar.html"), name='ins_cargo'),
    path('personal_edu/detalle_personal/<int:pk>', personalDetalle.as_view(template_name = "Personal/personal_detalle.html"), name='det_cargo'),
    path('personal_edu/editar_personal/<int:pk>', personalActualizar.as_view(template_name = "Personal/personal_actualizar.html"), name='actu_cargo'),
    path('personal_edu/eliminar_personal/<int:pk>', personalEliminar.as_view(), name='elim_personal'),
    # Urls para todo lo relacionado a estudiantes
    path('estudiantes/', alumnosListado.as_view(template_name = "Estudiantes/estudiantes.html"), name='leer'),
    path('estudiantes/insertar', alumnoInsertar.as_view(template_name = "Estudiantes/insertar_estudiante.html"), name='insertar'),
    path('estudiantes/detalle/<int:pk>', alumnoDetalle.as_view(template_name = "Estudiantes/detalles_estudiante.html"), name='detalle'),
    path('estudiantes/editar/<int:pk>', alumnoActualizar.as_view(template_name = "Estudiantes/alumno_actualizar.html"), name='actualizar'),
    path('estudiantes/eliminar/<int:pk>', alumnoEliminar.as_view(), name='elim_estudiante'),
    # Urls para todo lo relacionado a niveles educativos
    path('niveles_edu/', nivelListado.as_view(template_name = "Niveles/niveles.html"), name='list_nivel'),
    path('niveles_edu/insert_nivel', nivelInsertar.as_view(template_name = "Niveles/insertar_nivel.html"), name='ins_nivel'),
    path('niveles_edu/detalle_nivel/<int:pk>', nivelDetalle.as_view(template_name = "Niveles/detalles_nivel.html"), name='det_nivel'),
    path('niveles_edu/editar_nivel/<int:pk>', nivelActualizar.as_view(template_name = "Niveles/actualizar_nivel.html"), name='actu_nivel'),
    path('niveles_edu/eliminar_nivel/<int:pk>', nivelEliminar.as_view(), name='elim_nivel'),
    # Urls para todo lo relacionado a carreras educativas
    path('carreras_nivel/', carreraListado.as_view(template_name = "Carreras/carreras.html"), name='list_carrera'),
    path('carreras_nivel/insert_carrera', carreraInsertar.as_view(template_name = "Carreras/insertar_carrera.html"), name='ins_nivel'),
    path('carreras_nivel/detalle_carrera/<int:pk>', carreraDetalle.as_view(template_name = "Carreras/detalles_carrera.html"), name='det_nivel'),
    path('carreras_nivel/editar_carrera/<int:pk>', carreraActualizar.as_view(template_name = "Carreras/actualizar_carrera.html"), name='actu_nivel'),
    path('carreras_nivel/eliminar_carrera/<int:pk>', carreraEliminar.as_view(), name='elim_carrera'),
    # Urls para todo lo relacionado a carreras educativas
    path('grados/', gradoListado.as_view(template_name = "Grados/grados.html"), name='list_grado'),
    path('grados/insert_grado', gradoInsertar.as_view(template_name = "Grados/insertar_grado.html"), name='ins_grado'),
    path('grados/detalle_grado/<int:pk>', gradoDetalle.as_view(template_name = "Grados/detalles_grado.html"), name='det_grado'),
    path('grados/editar_grado/<int:pk>', gradoActualizar.as_view(template_name = "Grados/actualizar_grado.html"), name='actu_grado'),
    path('grados/eliminar_grado/<int:pk>', gradoEliminar.as_view(), name='elim_grado'),
    # Urls para todo lo relacionado a carreras educativas
    path('carre_grados/', carrera_gradoListado.as_view(template_name = "Carrera_Grados/carreras_grados.html"), name='list_carrera_grado'),
    path('carre_grados/insert_c_grado', carrera_gradoInsertar.as_view(template_name = "Carrera_Grados/insertar_carre_grado.html"), name='ins_c_grado'),
    path('carre_grados/detalle_c_grado/<int:pk>', carrera_gradoDetalle.as_view(template_name = "Carrera_Grados/detalles_carre_grado.html"), name='det_c_grado'),
    path('carre_grados/editar_c_grado/<int:pk>', carrera_gradoActualizar.as_view(template_name = "Carrera_Grados/actualizar_carre_grado.html"), name='actu_c_grado'),
    path('carre_grados/eliminar_c_grado/<int:pk>', carrera_gradoEliminar.as_view(), name='elim_c_grados'),
    # Urls para todo lo relacionado a carreras educativas
    path('cursos/', cursoListado.as_view(template_name = "Cursos/cursos.html"), name='list_curso'),
    path('cursos/insert_curso', cursoInsertar.as_view(template_name = "Cursos/curso_insertar.html"), name='ins_curso'),
    path('cursos/detalle_curso/<int:pk>', cursoDetalle.as_view(template_name = "Cursos/curso_detalles.html"), name='det_curso'),
    path('cursos/editar_curso/<int:pk>', cursoActualizar.as_view(template_name = "Cursos/curso_actualizar.html"), name='actu_curso'),
    path('cursos/eliminar_curso/<int:pk>', cursoEliminar.as_view(), name='elim_curso'),
    # Urls para todo lo relacionado a carreras educativas
    path('grados_cursos/', grado_cursoListado.as_view(template_name = "Grados_Cursos/grados_cursos.html"), name='list_grado_curso'),
    path('grados_cursos/insert_grado_curso', grado_cursoInsertar.as_view(template_name = "Grados_Cursos/insertar_grado_curso.html"), name='ins_grado_curso'),
    path('grados_cursos/detalle_grado_curso/<int:pk>', grado_cursoDetalle.as_view(template_name = "Grados_Cursos/detalles_grado_curso.html"), name='det_grado_curso'),
    path('grados_cursos/editar_grado_curso/<int:pk>', grado_cursoActualizar.as_view(template_name = "Grados_Cursos/actualizar_grado_curso.html"), name='actu_grado_curso'),
    path('grados_cursos/eliminar_grado_curso/<int:pk>', grado_cursoEliminar.as_view(), name='elim_grado_curso'),
    # Urls para todo lo relacionado a los Tutores de los estudiantes
    path('tutores/', tutorListado.as_view(template_name = "Tutores/tutores.html"), name='list_tutor'),
    path('tutores/insert_tutor', tutorInsertar.as_view(template_name = "Tutores/tutor_insertar.html"), name='ins_tutor'),
    path('tutores/detalle_tutor/<int:pk>', tutorDetalle.as_view(template_name = "Tutores/tutor_detalles.html"), name='det_tutor'),
    path('tutores/editar_tutor/<int:pk>', tutorActualizar.as_view(template_name = "Tutores/tutor_actualizar.html"), name='actu_tutor'),
    path('tutores/eliminar_tutor/<int:pk>', tutorEliminar.as_view(), name='elim_tutor'),
    # Urls para todo lo relacionado a carreras educativas
    path('alumno_cursos/', estudiante_cursoListado.as_view(template_name = "Estudiantes_Cursos/estudiantes_cursos.html"), name='list_alumno_curso'),
    path('alumno_cursos/insert_alumno_curso', estudiante_cursoInsertar.as_view(template_name = "Estudiantes_Cursos/insertar_estudiante_curso.html"), name='ins_estu_curso'),
    path('alumno_cursos/detalle_alumno_curso/<int:pk>', estudiante_cursoDetalle.as_view(template_name = "Estudiantes_Cursos/detalles_estudiante_curso.html"), name='det_estu_curso'),
    path('alumno_cursos/editar_alumno_curso/<int:pk>', estudiante_cursoActualizar.as_view(template_name = "Estudiantes_Cursos/actualizar_estudiante_curso.html"), name='actu_estu_curso'),
    path('alumno_cursos/eliminar_alumno_curso/<int:pk>', estudiante_cursoEliminar.as_view(), name='elim_estudiante_curso'),
# Urls para todo lo relacionado a las notas para los estudiantes
    path('notas/', notasListado.as_view(template_name = "Notas/notas.html"), name='list_notas'),
    path('notas/insert_notas', notasInsertar.as_view(template_name = "Notas/notas_insertar.html"), name='ins_notas'),
    path('notas/detalle_notas/<int:pk>', notasDetalle.as_view(template_name = "Notas/notas_detalle.html"), name='det_notas'),
    path('notas/editar_notas/<int:pk>', notasActualizar.as_view(template_name = "Notas/notas_actualizar.html"), name='actu_notas'),
    path('notas/eliminar_notas/<int:pk>', notasEliminar.as_view(), name='elim_notas'),
    # Urls para todo lo relacionado a las notas para los estudiantes
    path('colegiaturas/', colegiaturaListado.as_view(template_name = "Colegiaturas/colegiaturas.html"), name='list_colegiaturas'),
    path('colegiaturas/insert_colegiatura', colegiaturaInsertar.as_view(template_name = "Colegiaturas/colegiaturas_insertar.html"), name='ins_colegiaturas'),
    path('colegiaturas/detalle_colegiatura/<int:pk>', colegiaturaDetalle.as_view(template_name = "Colegiaturas/colegiaturas_detalle.html"), name='det_colegiaturas'),
    path('colegiaturas/editar_colegiatura/<int:pk>', colegiaturaActualizar.as_view(template_name = "Colegiaturas/colegiaturas_actualizar.html"), name='actu_colegiaturas'),
    path('colegiaturas/eliminar_colegiatura/<int:pk>', colegiaturaEliminar.as_view(), name='elim_colegiatura'),
]
