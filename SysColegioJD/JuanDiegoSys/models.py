# C:\Users\HP\ProyectosWeb\ProyColegio\lib\site-packages\pymysql\__init__.py
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
# from django.db import Sum
from django.db.models import Sum
from django.db.models import F, FloatField, Sum
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager, AbstractUser)

# Create your models here.

# Inicio de Modelos para la App
class Cargos(models.Model):
    cargo = models.CharField(db_column='Cargo', max_length=50)  # Field name made lowercase.
    desc_cargo = models.CharField(db_column='Descripcion', max_length=60)  # Field name made lowercase.
    def __str__(self):
        return self.cargo
    class Meta:
        db_table = 'cargos'
        ordering = ['cargo']

class Personal(models.Model):
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE) #Llamada a la tabla Cargos (Clave Foranea)
    personal_nombres = models.CharField(db_column='Personal_Nombres', max_length=45)  # Field name made lowercase.
    personal_apellidos = models.CharField(db_column='Personal_Apellidos', max_length=45)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=12)  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion', auto_now_add=True)  # Field name made lowercase.
    salario = models.FloatField(db_column='Salario', blank=True, null=True)  # Field name made lowercase.
    def __str__ (self):
    		return self.personal_nombres
    class Meta:
        db_table = 'personal'
        ordering = ['personal_apellidos']

# Función para registrar personal de la institución

class ManejadorUsuario(BaseUserManager):

    def create_user(self, correo, password=None):
        if not correo:
            raise ValueError('Usuarios deben tener un correo electrónico válido.')

        usuario = self.model(
            correo=self.normalize_email(correo),
        )
        usuario.set_password(password)
        usuario.save(using = self._db)
        return usuario

    def create_staffuser(self, correo, password):
        usuario = self.create_user(
            correo,
            password=password,
        )
        usuario.staff = True
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, password):
        usuario = self.create_user(
            correo,
            password=password,
        )
        usuario.staff = True
        usuario.admin = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractUser):
    # cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)  # Llamada a la tabla Cargos (Clave Foranea)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo = models.EmailField(verbose_name='correo electrónico', max_length=100, unique=True)
    active = models.BooleanField('Activo', default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('usuario')
        verbose_name_plural = ('usuarios')

    def get_full_name(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno

    def get_short_name(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        "¿El usuario cuenta con un permiso en específico?"
        return True

    def has_module_perms(self, app_label):
        "¿El usuario cuenta con los permisos para ver una app en específico?"
        return True

    @property
    def is_staff(self):
        "¿El usuario es staff (no super-usuario)?"
        return self.staff

    @property
    def is_admin(self):
        "¿El usuario es un administrador (super-usuario)?"
        return self.admin

    @property
    def is_active(self):
        "¿El usuario está activo?"
        return self.active

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.correo

# Fin model para usuarios

class Accesos(models.Model): # crear vistas, urls, y archivos.html para este instancia
    personal_id_personal = models.ForeignKey(Personal, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea)
    user = models.CharField(db_column='User', max_length=15)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=25)  # Field name made lowercase.

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'accesos'

class NivelesEducativos(models.Model):
    nombre_nivel = models.CharField(db_column='Nombre_Nivel', max_length=25)  # Field name made lowercase.
    def __str__(self):
        return self.nombre_nivel
    class Meta:
        db_table = 'niveles_educativos'

class Carreras(models.Model):
    nivele_educativo_id_nivel = models.ForeignKey(NivelesEducativos, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea)
    nombre_carrera = models.CharField(db_column='Nombre_Carrera', max_length=90)  # Field name made lowercase.
    def __str__(self):
        return self.nombre_carrera
    class Meta:
        db_table = 'carreras'

class Grados(models.Model):
    nombre_grado = models.CharField(db_column='Nombre_Grado', max_length=20)  # Field name made lowercase.
    seccion_grado = models.CharField(db_column='Seccion_Grado', max_length=3)  # Field name made lowercase
    def __str__(self):
        return '%s %s' % (self.nombre_grado, self.seccion_grado)
    class Meta:
        db_table = 'grados'

class CarrerasGrados(models.Model):
    carreras_id_carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea)
    grados_id_grado = models.ForeignKey(Grados, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea)
    def __str__(self):
        return self.carreras_id_carrera
    class Meta:
        db_table = 'carreras_grados'

class Cursos(models.Model):
    codigo_curso = models.CharField(db_column='Codigo_Curso', max_length=10, blank=True, null=True)  # Field name made lowercase.
    personal_id_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)  # Field name made lowercase.
    nombre_curso = models.CharField(db_column='Nombre_Curso', max_length=30)  # Field name made lowercase.
    descripcion_curso = models.CharField(db_column='Descripcion_Curso', max_length=50, blank=True, null=True)  # Field name made lowercase.
    horario_curso = models.TimeField(db_column='Horario_Curso')  # Field name made lowercase.
    periodos_diarios = models.IntegerField(db_column='Periodos_Diarios', blank=True, null=True)  # Field name made lowercase.
    periodos_semanales = models.IntegerField(db_column='Periodos_Semanales', blank=True, null=True )  # Field name made lowercase.
    def __str__(self):
        return self.nombre_curso
    class Meta:
        db_table = 'cursos'

class GradosCursos(models.Model):
    grados_id_grado = models.ForeignKey(Grados, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea)
    cursos_id_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea)
    def __str__(self):
        return self.grados_id_grado
    class Meta:
        db_table = 'grados_cursos'

class Tutores(models.Model):
    dpi_tutor = models.CharField(db_column='DPI_Tutor', max_length=14)  # Field name made lowercase.
    nombres_tutor = models.CharField(db_column='Nombres_Tutor', max_length=50)  # Field name made lowercase.
    apellidos_tutor = models.CharField(db_column='Apellidos_Tutor', max_length=50)  # Field name made lowercase.
    telefono_tutor = models.CharField(db_column='Telefono_Tutor', max_length=8, blank=True, null=True)  # Field name made lowercase.
    direccion_tutor = models.CharField(db_column='Direccion_Tutor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email_tutor = models.CharField(db_column='email_Tutor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='Fecha_Inscripcion', auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.nombres_tutor, self.apellidos_tutor)
    class Meta:
        db_table = 'tutores'
        ordering = ['apellidos_tutor']

class Estudiantes(models.Model):
    tutores_id_tutor = models.ForeignKey(Tutores, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    estudiante_codigo = models.CharField(db_column='Codigo', max_length=15)  # Field name made lowercase.
    estudiante_nombres = models.CharField(db_column='Estudiante_Nombres', max_length=50)  # Field name made lowercase.
    estudiante_apellidos = models.CharField(db_column='Estudiante_Apellidos', max_length=50)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento')  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100)  # Field name made lowercase.
    no_celular = models.CharField(db_column='No_Celular', max_length=8,blank=True, null=True )  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    tipo_genero = ( # Definción de opciones para ComboBox
        ('SG', 'Seleccione genero del Estudiante'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        )
    sexo = models.CharField(
    	max_length=2,
    	choices=tipo_genero,
    	default = 'SG',
    	)
    fecha_inscripcion = models.DateTimeField(db_column='Fecha_Inscripcion', auto_now_add=True)
    mensualidad = models.FloatField(db_column='Mensualidad')  # Field name made lowercase.
    def __str__(self):
        return '%s %s %s' % (self.estudiante_codigo, self.estudiante_nombres, self.estudiante_apellidos)
    class Meta:
        db_table = 'estudiantes'
        ordering = ['estudiante_apellidos']

class EstudianteCuros(models.Model):
    estudiantes_id_estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    cursos_id_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    def __str__(self):
        return self.estudiantes_id_estudiante
    class Meta:
        db_table = 'estudiante_curso'

class Notas(models.Model):
    estudiantes_id_estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    cursos_id_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    primer_parcial = models.FloatField(db_column='Primer_Parcial', default=0)  # Field name made lowercase.
    segundo_parcial = models.FloatField(db_column='Segundo_Parcial', default=0)  # Field name made lowercase.
    tercer_parcial = models.FloatField(db_column='Tercer_Parcial', default=0)  # Field name made lowercase.
    cuarto_parcial = models.FloatField(db_column='Cuarto_Parcial', default=0)  # Field name made lowercase.
    quinto_parcial = models.FloatField(db_column='Quinto_Parcial', default=0)  # Field name made lowercase.
    nota_final = models.FloatField(db_column='Nota_Final', default=0)  # Field name made lowercase.

    def __str__(self):
        return self.estudiantes_id_estudiante

    def save(self, *args, **kwargs):
        total = (Notas.objects.filter(Notas).aggregate(
            total=Sum('primer_parcial', field="primer_parcial+segundo_parcial"))
        ['total']
        )
        super(Notas, self).save(*args, **kwargs)

    def add_function(primer_parcial, segundo_parcial, tercer_parcial, cuarto_parcial, quinto_parcial):
        nota_final = primer_parcial + segundo_parcial + tercer_parcial + cuarto_parcial + quinto_parcial
        return result

    class Meta:
        db_table = 'notas'

class MesesColegiatura(models.Model):
    nombre_mes = models.CharField(db_column='Nombre_Mes', max_length=12)  # Field name made lowercase.
    def __str__(self):
        return self.nombre_mes
    class Meta:
        db_table = 'meses_colegiaturas'

class Transacestudiantes(models.Model):
    personal_id_personal = models.ForeignKey(Personal, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    tutores_id_tutor = models.ForeignKey(Tutores, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    estudiantes_id_estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE) #Llamada a la tabla Cliente (Clave Foranea
    colegiaturas_id_mes = models.ForeignKey(MesesColegiatura, on_delete=models.CASCADE, blank=True, null=True) #Llamada a la tabla Cliente (Clave Foranea
    fecha_transaccion = models.DateTimeField(auto_now_add=True, db_column='Fecha_Transaccion')  # Field name made lowercase.
    cantidadtotal = models.FloatField(db_column='CantidadTotal')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    def __str__(self):
        return '%s %s' % (self.colegiaturas_id_mes, estudiantes_id_estudiante)
    class Meta:
        db_table = 'transac_estudiantes'