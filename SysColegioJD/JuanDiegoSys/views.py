from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .models import NivelesEducativos, Estudiantes, Carreras, Cargos, Personal, Grados, CarrerasGrados, Cursos,\
    GradosCursos, Tutores, EstudianteCuros, Notas, Transacestudiantes
from django.views.generic import ListView, DetailView, TemplateView

# ejemplo 2
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# ejemplo 1
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
# Nuevas librerías
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    """
    This view redirects user to home if logged in else it redirects user
    to login page.
    """

    if request.user.is_authenticated:
        return HttpResponseRedirect('home')
    return HttpResponseRedirect('login')

@login_required
def home(request):
    """
    This renders the home page.
    """

    return render(request, "main.html")


def login_view(request):
    """
    Login view imported from templates.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect('home')
    next_url = request.GET.get('next', '/home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(next_url)
            return render(
                request, 'index.html',
                {'message': 'Usuario o contraseña de acceso incorrectos'}
            )
    return render(request, "index.html", {})


def logout_view(request):
    """
    Log out user to the login page.
    """

    logout(request)
    return HttpResponseRedirect('login')

# Inicio de vistas para el login
class homeNivelesEduView(TemplateView):
    template_name = 'home_niveles_edu.html'

class cargosPersonalView(TemplateView):
    template_name = 'home_cargos_personal.html'

class tutoresEstudiantesView(TemplateView):
    template_name = 'home_tutores_estudiantes.html'

class asignacionesView(TemplateView):
    template_name = 'home_asignaciones.html'

# Inicio de vistas para el proyecto

class AcercaView(TemplateView):
	template_name='Acerca_de.html'

# Usos de todo lo relacionado al Modelo para Niveles Educativos
class cargoListado(ListView):
    model = Cargos

class cargoDetalle(DetailView):
    model = Cargos

class cargoInsertar(SuccessMessageMixin, CreateView):
    model = Cargos
    form = Cargos
    fields = "__all__"
    success_message = 'Cargo educativo ingresado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
    def insertarCargo(request):
        if request.method == 'POST':
            form = Cargos(request.POST)
            if form.is_valid():
                cargo = form.cleaned_data['cargo']
                desc_cargo = form.cleaned_data['desc_cargo']
                cargos_personal = Cargos.objects.create(
                    cargo=cargo,
                    desc_cargo=desc_cargo)
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_cargo')  # Redireccionamos a la vista principal 'leer'

class cargoActualizar(SuccessMessageMixin, UpdateView):
    model = Cargos
    form = Cargos
    fields = "__all__"
    success_message = 'Datos del cargo educativo actualizados correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_cargo')  # Redireccionamos a la vista principal 'leer'

class cargoEliminar(SuccessMessageMixin, DeleteView):
    model = NivelesEducativos
    form = NivelesEducativos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Cargo eliminado correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_nivel')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para el Personal del Centro Educativo
class personalListado(ListView):
    model = Personal


class personalDetalle(DetailView):
    model = Personal


class personalInsertar(SuccessMessageMixin, CreateView):
    model = Personal
    form = Personal
    fields = "__all__"
    success_message = 'Personal del centro educativo ingresado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarPersonal(request):
        if request.method == 'POST':
            form = Personal(request.POST)
            if form.is_valid():
                cargo = form.cleaned_data['cargo']
                personal_nombres = form.cleaned_data['personal_nombres']
                personal_apellidos = form.cleaned_data['personal_apellidos']
                celular = form.cleaned_data['celular']
                email = form.cleaned_data['email']
                direccion = form.cleaned_data['direccion']
                fecha_creacion = form.cleaned_data['fecha_creacion']
                salario = form.cleaned_data['salario']
                cargos_personal = Personal.objects.create(
                    cargo=cargo,
                    personal_nombres=personal_nombres,
                    personal_apellidos=personal_apellidos,
                    celular=celular,
                    email=email,
                    direccion=direccion,
                    fecha_creacion=fecha_creacion,
                    salario=salario)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_personal')  # Redireccionamos a la vista principal 'leer'


class personalActualizar(SuccessMessageMixin, UpdateView):
    model = Personal
    form = Personal
    fields = ['cargo', 'personal_nombres', 'personal_apellidos', 'celular', 'email', 'direccion', 'salario']
    success_message = 'Datos del personal educativo actualizados correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_personal')  # Redireccionamos a la vista principal 'leer'


class personalEliminar(SuccessMessageMixin, DeleteView):
    model = Personal
    form = Personal
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Personal eliminado correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_personal')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para Niveles Educativos
class nivelListado(ListView):
    model = NivelesEducativos


class nivelDetalle(DetailView):
    model = NivelesEducativos


class nivelInsertar(SuccessMessageMixin, CreateView):
    model = NivelesEducativos
    form = NivelesEducativos
    fields = "__all__"
    success_message = 'Nivel Educativo ingresado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarNivel(request):
        if request.method == 'POST':
            form = NivelesEducativos(request.POST)
            if form.is_valid():
                nombre_nivel = form.cleaned_data['nombre_nivel']
                niveles_edu = NivelesEducativos.objects.create(
                    nombre_nivel=nombre_nivel)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_nivel')  # Redireccionamos a la vista principal 'leer'


class nivelActualizar(SuccessMessageMixin, UpdateView):
    model = NivelesEducativos
    form = NivelesEducativos
    fields = "__all__"
    success_message = 'Datos de alumno Actualizados Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_nivel')  # Redireccionamos a la vista principal 'leer'


class nivelEliminar(SuccessMessageMixin, DeleteView):
    model = NivelesEducativos
    form = NivelesEducativos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Nivel Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_nivel')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para todas las carreras existentes en el colegio
class carreraListado(ListView):
    model = Carreras


class carreraDetalle(DetailView):
    model = Carreras


class carreraInsertar(SuccessMessageMixin, CreateView):
    model = Carreras
    form = Carreras
    fields = "__all__"
    success_message = 'Carrera Educativo ingresado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarNivel(request):
        if request.method == 'POST':
            form = Carreras(request.POST)
            if form.is_valid():
                nombre_nivel = form.cleaned_data['nombre_nivel']
                niveles_edu = Carreras.objects.create(
                    nombre_nivel=nombre_nivel)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_carrera')  # Redireccionamos a la vista principal 'leer'


class carreraActualizar(SuccessMessageMixin, UpdateView):
    model = Carreras
    form = Carreras
    fields = "__all__"
    success_message = 'Datos de la Carrera Actualizados Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_carrera')  # Redireccionamos a la vista principal 'leer'


class carreraEliminar(SuccessMessageMixin, DeleteView):
    model = NivelesEducativos
    form = NivelesEducativos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Carrera Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_nivel')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para todos los grados educativos existentes
class gradoListado(ListView):
    model = Grados


class gradoDetalle(DetailView):
    model = Grados


class gradoInsertar(SuccessMessageMixin, CreateView):
    model = Grados
    form = Grados
    fields = "__all__"
    success_message = 'Grado Educativo ingresado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarGrado(request):
        if request.method == 'POST':
            form = Grados(request.POST)
            if form.is_valid():
                nombre_grado = form.cleaned_data['nombre_grado']
                seccion_grado = form.cleaned_data['seccion_grado']
                niveles_edu = Grados.objects.create(
                    nombre_grado=nombre_grado,
                    seccion_grado=seccion_grado)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_grado')  # Redireccionamos a la vista principal 'leer'


class gradoActualizar(SuccessMessageMixin, UpdateView):
    model = Grados
    form = Grados
    fields = "__all__"
    success_message = 'Datos del grado Actualizados Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_grado')  # Redireccionamos a la vista principal 'leer'


class gradoEliminar(SuccessMessageMixin, DeleteView):
    model = Grados
    form = Grados
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Grado Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_nivel')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para los Cursos de cada Carreras y Grados Académico
class carrera_gradoListado(ListView):
    model = CarrerasGrados


class carrera_gradoDetalle(DetailView):
    model = CarrerasGrados


class carrera_gradoInsertar(SuccessMessageMixin, CreateView):
    model = CarrerasGrados
    form = CarrerasGrados
    fields = "__all__"
    success_message = 'Asignación de carrera y grado registrado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarCarrera_Grado(request):
        if request.method == 'POST':
            form = CarrerasGrados(request.POST)
            if form.is_valid():
                carreras_id_carrera = form.cleaned_data['carreras_id_carrera']
                grados_id_grado = form.cleaned_data['grados_id_grado']
                carre_grados = CarrerasGrados.objects.create(
                    carreras_id_carrera=carreras_id_carrera,
                    grados_id_grado=grados_id_grado)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_carrera_grado')  # Redireccionamos a la vista principal 'leer'


class carrera_gradoActualizar(SuccessMessageMixin, UpdateView):
    model = CarrerasGrados
    form = CarrerasGrados
    fields = "__all__"
    success_message = 'Asignación de Carrera y grado Actualizados Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_carrera_grado')  # Redireccionamos a la vista principal 'leer'


class carrera_gradoEliminar(SuccessMessageMixin, DeleteView):
    model = CarrerasGrados
    form = CarrerasGrados
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Asignación de Carrera y Grado Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_carrera_grado')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para los Cursos de cada Carreras y Grados Académico
class cursoListado(ListView):
    model = Cursos


class cursoDetalle(DetailView):
    model = Cursos


class cursoInsertar(SuccessMessageMixin, CreateView):
    model = Cursos
    form = Cursos
    fields = "__all__"
    success_message = 'Curso registrado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarCurso(request):
        if request.method == 'POST':
            form = Cursos(request.POST)
            if form.is_valid():
                codigo_curso = form.cleaned_data['codigo_curso']
                personal_id_personal = form.cleaned_data['personal_id_personal']
                nombre_curso = form.cleaned_data['nombre_curso']
                descripcion_curso = form.cleaned_data['descripcion_curso']
                horario_curso = form.cleaned_data['horario_curso']
                periodos_diarios = form.cleaned_data['periodos_diarios']
                periodos_semanales = form.cleaned_data['periodos_semanales']
                curso = Cursos.objects.create(
                    codigo_curso=codigo_curso,
                    personal_id_personal=personal_id_personal,
                    nombre_curso=nombre_curso,
                    descripcion_curso=descripcion_curso,
                    horario_curso=horario_curso,
                    periodos_diarios=periodos_diarios,
                    periodos_semanales=periodos_semanales)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_curso')  # Redireccionamos a la vista principal 'leer'


class cursoActualizar(SuccessMessageMixin, UpdateView):
    model = Cursos
    form = Cursos
    fields = "__all__"
    success_message = 'Datos del cruso actualizados correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_curso')  # Redireccionamos a la vista principal 'leer'


class cursoEliminar(SuccessMessageMixin, DeleteView):
    model = Cursos
    form = Cursos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Curso eliminado correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_curso')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para Asignar Grados y Cursos
class grado_cursoListado(ListView):
    model = GradosCursos


class grado_cursoDetalle(DetailView):
    model = GradosCursos


class grado_cursoInsertar(SuccessMessageMixin, CreateView):
    model = GradosCursos
    form = GradosCursos
    fields = "__all__"
    success_message = 'Asignación de grado y curso registrado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarGrado_Curso(request):
        if request.method == 'POST':
            form = GradosCursos(request.POST)
            if form.is_valid():
                grados_id_grado = form.cleaned_data['grados_id_grado']
                cursos_id_curso = form.cleaned_data['cursos_id_curso']
                carre_grados = GradosCursos.objects.create(
                    grados_id_grado=grados_id_grado,
                    cursos_id_curso=cursos_id_curso)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_grado_curso')  # Redireccionamos a la vista principal 'leer'


class grado_cursoActualizar(SuccessMessageMixin, UpdateView):
    model = GradosCursos
    form = GradosCursos
    fields = "__all__"
    success_message = 'Asignación de grado y curso Actualizados Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_grado_curso')  # Redireccionamos a la vista principal 'leer'


class grado_cursoEliminar(SuccessMessageMixin, DeleteView):
    model = GradosCursos
    form = GradosCursos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Asignación de Grado y Curso Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_grado_curso')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para los Tutores o Responsable de los Estudiantes
class tutorListado(ListView):
    model = Tutores


class tutorDetalle(DetailView):
    model = Tutores


class tutorInsertar(SuccessMessageMixin, CreateView):
    model = Tutores
    form = Tutores
    fields = "__all__"
    success_message = 'Tutor registrado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarTutor(request):
        if request.method == 'POST':
            form = Tutores(request.POST)
            if form.is_valid():
                dpi_tutor = form.cleaned_data['dpi_tutor']
                nombres_tutor = form.cleaned_data['nombres_tutor']
                apellidos_tutor = form.cleaned_data['apellidos_tutor']
                telefono_tutor = form.cleaned_data['telefono_tutor']
                direccion_tutor = form.cleaned_data['direccion_tutor']
                email_tutor = form.cleaned_data['periodos_semanales']
                fecha_creacion = form.cleaned_data['periodos_semanales']
                tutor = Tutores.objects.create(
                    dpi_tutor=dpi_tutor,
                    nombres_tutor=nombres_tutor,
                    apellidos_tutor=apellidos_tutor,
                    telefono_tutor=telefono_tutor,
                    direccion_tutor=direccion_tutor,
                    email_tutor=email_tutor,
                    fecha_creacion=fecha_creacion)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_tutor')  # Redireccionamos a la vista principal 'leer'


class tutorActualizar(SuccessMessageMixin, UpdateView):
    model = Tutores
    form = Tutores
    fields = "__all__"
    success_message = 'Datos del tutor actualizados correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_tutor')  # Redireccionamos a la vista principal 'leer'


class tutorEliminar(SuccessMessageMixin, DeleteView):
    model = Tutores
    form = Tutores
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Tutor eliminado correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_tutor')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para Estudiantes
class alumnosListado(ListView):
    model = Estudiantes


class alumnoDetalle(DetailView):
    model = Estudiantes


class alumnoInsertar(SuccessMessageMixin, CreateView):
    model = Estudiantes
    form = Estudiantes
    fields = "__all__"
    success_message = 'Datos del Estudiante ingresados correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarEstudiante(request):
        if request.method == 'POST':
            form = Estudiantes(request.POST)
            if form.is_valid():
                tutores_id_tutor = form.cleaned_data['tutores_id_ttutor']
                estudiante_codigo = form.cleaned_data['estudiante_codigo']
                estudiante_nombres = form.cleaned_data['estudiante_nombres']
                estudiante_apellidos = form.cleaned_data['estudiante_apellidos']
                fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
                direccion = form.cleaned_data['direccion']
                no_celular = form.cleaned_data['no_celular']
                email = form.cleaned_data['email']
                sexo = form.cleaned_data['sexo']
                fecha_inscripcion = form.cleaned_data['fecha_inscripcion']
                mensualidad = form.cleaned_data['mensualidad']
                estudiante = Estudiantes.objects.create(
                    tutores_id_tutor=tutores_id_ttutor,
                    estudiante_codigo=estudiante_codigo,
                    estudiante_nombres=estudiante_nombres,
                    estudiante_apellidos=estudiante_apellidos,
                    fecha_nacimiento=fecha_nacimiento,
                    direccion=direccion,
                    no_celular=no_celular,
                    email=email,
                    sexo=sexo,
                    fecha_inscripcion=fecha_inscripcion,
                    mensualidad=mensualidad)

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class alumnoActualizar(SuccessMessageMixin, UpdateView):
    model = Estudiantes
    form = Estudiantes
    fields = "__all__"
    success_message = 'Datos de alumno Actualizados Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class alumnoEliminar(SuccessMessageMixin, DeleteView):
    model = Estudiantes
    form = Estudiantes
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Estudiante Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para Asignar Estudiantes y Cursos
class estudiante_cursoListado(ListView):
    model = EstudianteCuros


class estudiante_cursoDetalle(DetailView):
    model = EstudianteCuros


class estudiante_cursoInsertar(SuccessMessageMixin, CreateView):
    model = EstudianteCuros
    form = EstudianteCuros
    fields = "__all__"
    success_message = 'Asignación de curso a estudiante realizado correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarGrado_Curso(request):
        if request.method == 'POST':
            form = EstudianteCuros(request.POST)
            if form.is_valid():
                estudiantes_id_estudiante = form.cleaned_data['estudiantes_id_estudiante']
                cursos_id_curso = form.cleaned_data['cursos_id_curso']
                carre_grados = EstudianteCuros.objects.create(
                    estudiantes_id_estudiante=estudiantes_id_estudiante,
                    cursos_id_curso=cursos_id_curso)

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('list_alumno_curso')  # Redireccionamos a la vista principal 'leer'


class estudiante_cursoActualizar(SuccessMessageMixin, UpdateView):
    model = EstudianteCuros
    form = EstudianteCuros
    fields = "__all__"
    success_message = 'Asignación de curso a estudiante actualizados correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_alumno_curso')  # Redireccionamos a la vista principal 'leer'


class estudiante_cursoEliminar(SuccessMessageMixin, DeleteView):
    model = EstudianteCuros
    form = EstudianteCuros
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Asignación de curso a estudiante eliminado correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_alumno_curso')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para Notas de los alumnos en cada materia
class notasListado(ListView):
    model = Notas

class notasDetalle(DetailView):
    model = Notas

class notasInsertar(SuccessMessageMixin, CreateView):
    model = Notas
    form = Notas
    fields = "__all__"
    success_message = 'Datos del Estudiante ingresados correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarNotas(request):
        if request.method == 'POST':
            form = Notas(request.POST)
            if form.is_valid():
                estudiantes_id_estudiante = form.cleaned_data['estudiantes_id_estudiante']
                cursos_id_curso = form.cleaned_data['cursos_id_curso']
                primer_parcial = form.cleaned_data['primer_parcial']
                segundo_parcial = form.cleaned_data['segundo_parcial']
                tercer_parcial = form.cleaned_data['tercer_parcial']
                cuarto_parcial = form.cleaned_data['cuarto_parcial']
                quinto_parcial = form.cleaned_data['quinto_parcial']
                nota_final = form.cleaned_data['nota_final']
                notas = Notas.objects.create(
                    estudiantes_id_estudiante=estudiantes_id_estudiante,
                    cursos_id_curso=cursos_id_curso,
                    primer_parcial=primer_parcial,
                    segundo_parcial=segundo_parcial,
                    tercer_parcial=tercer_parcial,
                    cuarto_parcial=cuarto_parcial,
                    quinto_parcial=quinto_parcial,
                    nota_final=nota_final)
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('list_notas')  # Redireccionamos a la vista principal 'leer'

class notasActualizar(SuccessMessageMixin, UpdateView):
    model = Notas
    form = Notas
    fields = "__all__"
    success_message = 'Datos de alumno Actualizados Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_notas')  # Redireccionamos a la vista principal 'leer'

class notasEliminar(SuccessMessageMixin, DeleteView):
    model = Notas
    form = Notas
    fields = "__all__"
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Nota(s) del estudiante Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_notas')  # Redireccionamos a la vista principal 'leer'


# Usos de todo lo relacionado al Modelo para Tranac_Estudiantes
class colegiaturaListado(ListView):
    model = Transacestudiantes

class colegiaturaDetalle(DetailView):
    model = Transacestudiantes

class colegiaturaInsertar(SuccessMessageMixin, CreateView):
    model = Transacestudiantes
    form = Transacestudiantes
    fields = "__all__"
    success_message = 'Datos de la colegiatura ingresados correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    def insertarColegiatura(request):
        if request.method == 'POST':
            form = Transacestudiantes(request.POST)
            if form.is_valid():
                personal_id_personal = form.cleaned_data['personal_id_personal']
                tutores_id_tutor = form.cleaned_data['tutores_id_tutor']
                colegiaturas_id_mes = form.cleaned_data['colegiaturas_id_mes']
                estudiantes_id_estudiante = form.cleaned_data['estudiantes_id_estudiante']
                fecha_transaccion = form.cleaned_data['fecha_transaccion']
                cantidadtotal = form.cleaned_data['cantidadtotal']
                descripcion = form.cleaned_data['descripcion']
                colegiaturas = Transacestudiantes.objects.create(
                    personal_id_personal=personal_id_personal,
                    tutores_id_tutor=tutores_id_tutor,
                    estudiantes_id_estudiante=estudiantes_id_estudiante,
                    colegiaturas_id_mes=colegiaturas_id_mes,
                    fecha_transaccion=fecha_transaccion,
                    cantidadtotal=cantidadtotal,
                    descripcion=descripcion)
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('list_colegiaturas')  # Redireccionamos a la vista principal 'leer'

class colegiaturaActualizar(SuccessMessageMixin, UpdateView):
    model = Transacestudiantes
    form = Transacestudiantes
    fields = "__all__"
    success_message = 'Datos de la colegiatura actualizados correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('list_colegiaturas')  # Redireccionamos a la vista principal 'leer'

class colegiaturaEliminar(SuccessMessageMixin, DeleteView):
    model = Transacestudiantes
    form = Transacestudiantes
    fields = "__all__"
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Registro de colegiatura aliminada correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('list_colegiaturas')  # Redireccionamos a la vista principal 'leer'