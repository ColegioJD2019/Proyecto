-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-11-2019 a las 06:53:52
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbweb_colejd2019`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accesos`
--

CREATE TABLE `accesos` (
  `id` int(11) NOT NULL,
  `User` varchar(15) COLLATE latin1_spanish_ci NOT NULL,
  `Password` varchar(25) COLLATE latin1_spanish_ci NOT NULL,
  `personal_id_personal_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add cargos', 1, 'add_cargos'),
(2, 'Can change cargos', 1, 'change_cargos'),
(3, 'Can delete cargos', 1, 'delete_cargos'),
(4, 'Can view cargos', 1, 'view_cargos'),
(5, 'Can add carreras', 2, 'add_carreras'),
(6, 'Can change carreras', 2, 'change_carreras'),
(7, 'Can delete carreras', 2, 'delete_carreras'),
(8, 'Can view carreras', 2, 'view_carreras'),
(9, 'Can add cursos', 3, 'add_cursos'),
(10, 'Can change cursos', 3, 'change_cursos'),
(11, 'Can delete cursos', 3, 'delete_cursos'),
(12, 'Can view cursos', 3, 'view_cursos'),
(13, 'Can add estudiantes', 4, 'add_estudiantes'),
(14, 'Can change estudiantes', 4, 'change_estudiantes'),
(15, 'Can delete estudiantes', 4, 'delete_estudiantes'),
(16, 'Can view estudiantes', 4, 'view_estudiantes'),
(17, 'Can add grados', 5, 'add_grados'),
(18, 'Can change grados', 5, 'change_grados'),
(19, 'Can delete grados', 5, 'delete_grados'),
(20, 'Can view grados', 5, 'view_grados'),
(21, 'Can add niveles educativos', 6, 'add_niveleseducativos'),
(22, 'Can change niveles educativos', 6, 'change_niveleseducativos'),
(23, 'Can delete niveles educativos', 6, 'delete_niveleseducativos'),
(24, 'Can view niveles educativos', 6, 'view_niveleseducativos'),
(25, 'Can add personal', 7, 'add_personal'),
(26, 'Can change personal', 7, 'change_personal'),
(27, 'Can delete personal', 7, 'delete_personal'),
(28, 'Can view personal', 7, 'view_personal'),
(29, 'Can add tutores', 8, 'add_tutores'),
(30, 'Can change tutores', 8, 'change_tutores'),
(31, 'Can delete tutores', 8, 'delete_tutores'),
(32, 'Can view tutores', 8, 'view_tutores'),
(33, 'Can add transacestudiantes', 9, 'add_transacestudiantes'),
(34, 'Can change transacestudiantes', 9, 'change_transacestudiantes'),
(35, 'Can delete transacestudiantes', 9, 'delete_transacestudiantes'),
(36, 'Can view transacestudiantes', 9, 'view_transacestudiantes'),
(37, 'Can add notas', 10, 'add_notas'),
(38, 'Can change notas', 10, 'change_notas'),
(39, 'Can delete notas', 10, 'delete_notas'),
(40, 'Can view notas', 10, 'view_notas'),
(41, 'Can add grados cursos', 11, 'add_gradoscursos'),
(42, 'Can change grados cursos', 11, 'change_gradoscursos'),
(43, 'Can delete grados cursos', 11, 'delete_gradoscursos'),
(44, 'Can view grados cursos', 11, 'view_gradoscursos'),
(45, 'Can add estudiante curos', 12, 'add_estudiantecuros'),
(46, 'Can change estudiante curos', 12, 'change_estudiantecuros'),
(47, 'Can delete estudiante curos', 12, 'delete_estudiantecuros'),
(48, 'Can view estudiante curos', 12, 'view_estudiantecuros'),
(49, 'Can add carreras grados', 13, 'add_carrerasgrados'),
(50, 'Can change carreras grados', 13, 'change_carrerasgrados'),
(51, 'Can delete carreras grados', 13, 'delete_carrerasgrados'),
(52, 'Can view carreras grados', 13, 'view_carrerasgrados'),
(53, 'Can add accesos', 14, 'add_accesos'),
(54, 'Can change accesos', 14, 'change_accesos'),
(55, 'Can delete accesos', 14, 'delete_accesos'),
(56, 'Can view accesos', 14, 'view_accesos'),
(57, 'Can add log entry', 15, 'add_logentry'),
(58, 'Can change log entry', 15, 'change_logentry'),
(59, 'Can delete log entry', 15, 'delete_logentry'),
(60, 'Can view log entry', 15, 'view_logentry'),
(61, 'Can add permission', 16, 'add_permission'),
(62, 'Can change permission', 16, 'change_permission'),
(63, 'Can delete permission', 16, 'delete_permission'),
(64, 'Can view permission', 16, 'view_permission'),
(65, 'Can add group', 17, 'add_group'),
(66, 'Can change group', 17, 'change_group'),
(67, 'Can delete group', 17, 'delete_group'),
(68, 'Can view group', 17, 'view_group'),
(69, 'Can add user', 18, 'add_user'),
(70, 'Can change user', 18, 'change_user'),
(71, 'Can delete user', 18, 'delete_user'),
(72, 'Can view user', 18, 'view_user'),
(73, 'Can add content type', 19, 'add_contenttype'),
(74, 'Can change content type', 19, 'change_contenttype'),
(75, 'Can delete content type', 19, 'delete_contenttype'),
(76, 'Can view content type', 19, 'view_contenttype'),
(77, 'Can add session', 20, 'add_session'),
(78, 'Can change session', 20, 'change_session'),
(79, 'Can delete session', 20, 'delete_session'),
(80, 'Can view session', 20, 'view_session'),
(81, 'Can add meses colegiatura', 21, 'add_mesescolegiatura'),
(82, 'Can change meses colegiatura', 21, 'change_mesescolegiatura'),
(83, 'Can delete meses colegiatura', 21, 'delete_mesescolegiatura'),
(84, 'Can view meses colegiatura', 21, 'view_mesescolegiatura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE latin1_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE latin1_spanish_ci NOT NULL,
  `first_name` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE latin1_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE latin1_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$b4Ck0K6WVHNL$UKcGB+VjXS+yoWL8M7dWQ7q4DCLONENSut1wZbNvmuc=', '2019-11-05 22:07:29.601651', 1, 'AdminColegio', '', '', 'criskalelv@gmail.com', 1, 1, '2019-10-15 21:05:36.000000'),
(2, 'pbkdf2_sha256$150000$I7ZbZk3lt4MM$zadsy73poZzz9k0qMxLPyX3kXrPQimEbxGAkt/txioI=', '2019-10-29 14:20:27.000000', 0, 'docente1@gmail.com', '', '', '', 0, 0, '2019-10-29 14:19:49.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

CREATE TABLE `cargos` (
  `id` int(11) NOT NULL,
  `Cargo` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `Descripcion` varchar(60) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `cargos`
--

INSERT INTO `cargos` (`id`, `Cargo`, `Descripcion`) VALUES
(1, 'Director/a', 'Encargada de llevar el control de todo el centro educativo'),
(2, 'Sub-Director/a', 'Encargado de suplantar el puesto de la Directora del centro'),
(3, 'Secretario/a', 'Encargado/a de llevar los registros necesarios del centro'),
(4, 'Tesorero/a', 'Encargado/a de llevar el control de la parte económica'),
(5, 'Docente, Maestro/a, Profesor/a', 'Persona con cierto nivel educativo, que imparte conocimiento'),
(6, 'Conserje', 'Encargado de la limpieza del centro educativo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carreras`
--

CREATE TABLE `carreras` (
  `id` int(11) NOT NULL,
  `Nombre_Carrera` varchar(90) COLLATE latin1_spanish_ci NOT NULL,
  `nivele_educativo_id_nivel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `carreras`
--

INSERT INTO `carreras` (`id`, `Nombre_Carrera`, `nivele_educativo_id_nivel_id`) VALUES
(3, 'Básico Normal (3 años)', 1),
(5, 'Bachillerato en Ciencias y Letras con Orientación en Educación', 5),
(6, 'Bachillerato en Ciencias y Letras con Orientación en Ciencias Biológicas', 5),
(7, 'Bachillerato en Ciencias y Letras con Orientación en Educación Física', 5),
(8, 'Ingeniería', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carreras_grados`
--

CREATE TABLE `carreras_grados` (
  `id` int(11) NOT NULL,
  `carreras_id_carrera_id` int(11) NOT NULL,
  `grados_id_grado_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `carreras_grados`
--

INSERT INTO `carreras_grados` (`id`, `carreras_id_carrera_id`, `grados_id_grado_id`) VALUES
(1, 3, 1),
(3, 3, 2),
(4, 3, 3),
(5, 3, 4),
(6, 3, 5),
(7, 3, 6),
(8, 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `id` int(11) NOT NULL,
  `Nombre_Curso` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `Descripcion_Curso` varchar(50) COLLATE latin1_spanish_ci DEFAULT NULL,
  `Horario_Curso` time(6) NOT NULL,
  `Periodos_Diarios` int(11) DEFAULT NULL,
  `Periodos_Semanales` int(11) DEFAULT NULL,
  `personal_id_personal_id` int(11) NOT NULL,
  `Codigo_Curso` varchar(10) COLLATE latin1_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`id`, `Nombre_Curso`, `Descripcion_Curso`, `Horario_Curso`, `Periodos_Diarios`, `Periodos_Semanales`, `personal_id_personal_id`, `Codigo_Curso`) VALUES
(3, 'Matemáticas I', 'Aprendizaje de los números con primero básico', '13:00:00.000000', 2, 8, 3, 'MAT_001'),
(4, 'Matemáticas II', 'Aprendizaje de los números con segundo básico', '02:20:00.000000', 2, 8, 3, 'CURSO_02'),
(5, 'Psicología', NULL, '02:30:00.000000', 1, 4, 1, 'CURSO_89');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE latin1_spanish_ci,
  `object_repr` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE latin1_spanish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-10-29 14:14:46.800263', '1', 'AdminColegio', 2, '[]', 18, 1),
(2, '2019-10-29 14:19:49.489089', '2', 'docente1@gmail.com', 1, '[{\"added\": {}}]', 18, 1),
(3, '2019-10-29 14:22:32.198493', '2', 'docente1@gmail.com', 2, '[{\"changed\": {\"fields\": [\"is_active\"]}}]', 18, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(15, 'admin', 'logentry'),
(17, 'auth', 'group'),
(16, 'auth', 'permission'),
(18, 'auth', 'user'),
(19, 'contenttypes', 'contenttype'),
(14, 'JuanDiegoSys', 'accesos'),
(1, 'JuanDiegoSys', 'cargos'),
(2, 'JuanDiegoSys', 'carreras'),
(13, 'JuanDiegoSys', 'carrerasgrados'),
(3, 'JuanDiegoSys', 'cursos'),
(12, 'JuanDiegoSys', 'estudiantecuros'),
(4, 'JuanDiegoSys', 'estudiantes'),
(5, 'JuanDiegoSys', 'grados'),
(11, 'JuanDiegoSys', 'gradoscursos'),
(21, 'JuanDiegoSys', 'mesescolegiatura'),
(6, 'JuanDiegoSys', 'niveleseducativos'),
(10, 'JuanDiegoSys', 'notas'),
(7, 'JuanDiegoSys', 'personal'),
(9, 'JuanDiegoSys', 'transacestudiantes'),
(8, 'JuanDiegoSys', 'tutores'),
(20, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'JuanDiegoSys', '0001_initial', '2019-10-15 05:44:02.439788'),
(2, 'contenttypes', '0001_initial', '2019-10-15 05:44:04.611551'),
(3, 'auth', '0001_initial', '2019-10-15 05:44:05.002146'),
(4, 'admin', '0001_initial', '2019-10-15 05:44:06.236407'),
(5, 'admin', '0002_logentry_remove_auto_add', '2019-10-15 05:44:06.502030'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2019-10-15 05:44:06.533264'),
(7, 'contenttypes', '0002_remove_content_type_name', '2019-10-15 05:44:06.893300'),
(8, 'auth', '0002_alter_permission_name_max_length', '2019-10-15 05:44:07.033910'),
(9, 'auth', '0003_alter_user_email_max_length', '2019-10-15 05:44:07.127648'),
(10, 'auth', '0004_alter_user_username_opts', '2019-10-15 05:44:07.143273'),
(11, 'auth', '0005_alter_user_last_login_null', '2019-10-15 05:44:07.205777'),
(12, 'auth', '0006_require_contenttypes_0002', '2019-10-15 05:44:07.205777'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2019-10-15 05:44:07.221403'),
(14, 'auth', '0008_alter_user_username_max_length', '2019-10-15 05:44:07.346409'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2019-10-15 05:44:07.471398'),
(16, 'auth', '0010_alter_group_name_max_length', '2019-10-15 05:44:07.846380'),
(17, 'auth', '0011_update_proxy_permissions', '2019-10-15 05:44:07.908864'),
(18, 'sessions', '0001_initial', '2019-10-15 21:42:34.782616'),
(19, 'JuanDiegoSys', '0002_auto_20191016_2359', '2019-10-17 05:59:52.793324'),
(20, 'JuanDiegoSys', '0003_auto_20191017_0022', '2019-10-17 06:22:53.187482'),
(21, 'JuanDiegoSys', '0004_auto_20191017_0025', '2019-10-17 06:25:35.892527'),
(22, 'JuanDiegoSys', '0005_auto_20191017_0305', '2019-10-17 09:05:57.200706'),
(23, 'JuanDiegoSys', '0006_auto_20191017_0319', '2019-10-17 09:19:40.576696'),
(24, 'JuanDiegoSys', '0007_remove_cursos_grados_id_grado', '2019-10-17 16:06:50.776082'),
(25, 'JuanDiegoSys', '0008_cursos_codigo_curso', '2019-10-17 16:13:05.269605'),
(26, 'JuanDiegoSys', '0009_auto_20191021_1349', '2019-10-21 19:49:26.569255'),
(27, 'JuanDiegoSys', '0010_auto_20191024_0716', '2019-10-24 13:16:49.099716'),
(28, 'JuanDiegoSys', '0011_auto_20191028_1158', '2019-10-28 17:58:27.200549'),
(29, 'JuanDiegoSys', '0012_auto_20191028_1244', '2019-10-28 18:44:27.699399'),
(30, 'JuanDiegoSys', '0013_auto_20191028_1522', '2019-10-28 21:22:55.234917');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE latin1_spanish_ci NOT NULL,
  `session_data` longtext COLLATE latin1_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int(11) NOT NULL,
  `Codigo` varchar(15) COLLATE latin1_spanish_ci NOT NULL,
  `Estudiante_Nombres` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `Estudiante_Apellidos` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `Fecha_Nacimiento` date NOT NULL,
  `Direccion` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `No_Celular` varchar(8) COLLATE latin1_spanish_ci DEFAULT NULL,
  `email` varchar(50) COLLATE latin1_spanish_ci DEFAULT NULL,
  `sexo` varchar(2) COLLATE latin1_spanish_ci NOT NULL,
  `Fecha_Inscripcion` datetime(6) NOT NULL,
  `Mensualidad` double NOT NULL,
  `tutores_id_tutor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id`, `Codigo`, `Estudiante_Nombres`, `Estudiante_Apellidos`, `Fecha_Nacimiento`, `Direccion`, `No_Celular`, `email`, `sexo`, `Fecha_Inscripcion`, `Mensualidad`, `tutores_id_tutor_id`) VALUES
(1, 'ASDG_1234', 'Aldo Danilo', 'Marroquín Crisósotomo', '2000-10-12', 'Taltimiche, Comitancillo, San Marcos', '78907985', 'danilomarro@gmail.com', 'M', '2019-10-17 22:34:06.894799', 125.67, 1),
(2, 'HGDI_1233', 'Alberto Dionicio', 'López López', '1997-06-22', 'Taltimiche, Comitancillo, San Marcos', '13554236', 'humasl@gmail.com', 'M', '2019-10-28 18:17:14.242502', 234.5, 2),
(3, 'ASDG_1234', 'Aldo', 'Orozco', '1993-06-12', 'Tejutla, San Marcos', '67998897', 'dennis@gmail.com', 'M', '2019-11-02 22:46:57.849139', 234, 3),
(4, '135153-ASDF', 'Adalila', 'Fuentes', '1997-06-12', 'Tejutla, San Marcos', '78907985', 'carlos2019@hotmail.com', 'M', '2019-11-03 05:39:29.230544', 123, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante_curso`
--

CREATE TABLE `estudiante_curso` (
  `id` int(11) NOT NULL,
  `cursos_id_curso_id` int(11) NOT NULL,
  `estudiantes_id_estudiante_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `estudiante_curso`
--

INSERT INTO `estudiante_curso` (`id`, `cursos_id_curso_id`, `estudiantes_id_estudiante_id`) VALUES
(1, 3, 1),
(2, 4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grados`
--

CREATE TABLE `grados` (
  `id` int(11) NOT NULL,
  `Nombre_Grado` varchar(20) COLLATE latin1_spanish_ci NOT NULL,
  `Seccion_Grado` varchar(3) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `grados`
--

INSERT INTO `grados` (`id`, `Nombre_Grado`, `Seccion_Grado`) VALUES
(1, 'Primero', 'A'),
(2, 'Primero', 'B'),
(3, 'Segundo', 'A'),
(4, 'Segundo', 'B'),
(5, 'Tercero', 'A'),
(6, 'Tercero', 'B'),
(7, 'Primero', 'C');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grados_cursos`
--

CREATE TABLE `grados_cursos` (
  `id` int(11) NOT NULL,
  `cursos_id_curso_id` int(11) NOT NULL,
  `grados_id_grado_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `grados_cursos`
--

INSERT INTO `grados_cursos` (`id`, `cursos_id_curso_id`, `grados_id_grado_id`) VALUES
(1, 3, 1),
(2, 4, 3),
(3, 5, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `meses_colegiaturas`
--

CREATE TABLE `meses_colegiaturas` (
  `id` int(11) NOT NULL,
  `Nombre_Mes` varchar(12) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `meses_colegiaturas`
--

INSERT INTO `meses_colegiaturas` (`id`, `Nombre_Mes`) VALUES
(1, 'Inscripción'),
(2, 'Enero'),
(3, 'Febrero'),
(4, 'Marzo'),
(5, 'Abril'),
(6, 'Mayo'),
(7, 'Junio'),
(8, 'Julio'),
(9, 'Agosto'),
(10, 'Septiembre'),
(11, 'Octubre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `niveles_educativos`
--

CREATE TABLE `niveles_educativos` (
  `id` int(11) NOT NULL,
  `Nombre_Nivel` varchar(25) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `niveles_educativos`
--

INSERT INTO `niveles_educativos` (`id`, `Nombre_Nivel`) VALUES
(1, 'Nivel Básico'),
(5, 'Nivel Diversificado'),
(6, 'Nivel Pre-Primario'),
(7, 'Universidad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas`
--

CREATE TABLE `notas` (
  `id` int(11) NOT NULL,
  `Primer_Parcial` double NOT NULL,
  `Segundo_Parcial` double NOT NULL,
  `Tercer_Parcial` double NOT NULL,
  `Cuarto_Parcial` double NOT NULL,
  `Nota_Final` double NOT NULL,
  `cursos_id_curso_id` int(11) NOT NULL,
  `estudiantes_id_estudiante_id` int(11) NOT NULL,
  `Quinto_Parcial` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `notas`
--

INSERT INTO `notas` (`id`, `Primer_Parcial`, `Segundo_Parcial`, `Tercer_Parcial`, `Cuarto_Parcial`, `Nota_Final`, `cursos_id_curso_id`, `estudiantes_id_estudiante_id`, `Quinto_Parcial`) VALUES
(1, 12, 12, 13.5, 0, 0, 3, 1, 0),
(2, 12, 10, 0, 0, 0, 4, 2, 0),
(3, 11, 12, 0, 0, 0, 4, 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `id` int(11) NOT NULL,
  `Personal_Nombres` varchar(45) COLLATE latin1_spanish_ci NOT NULL,
  `Personal_Apellidos` varchar(45) COLLATE latin1_spanish_ci NOT NULL,
  `Celular` varchar(12) COLLATE latin1_spanish_ci NOT NULL,
  `email` varchar(50) COLLATE latin1_spanish_ci DEFAULT NULL,
  `direccion` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `Fecha_Creacion` datetime(6) NOT NULL,
  `Salario` double DEFAULT NULL,
  `cargo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `personal`
--

INSERT INTO `personal` (`id`, `Personal_Nombres`, `Personal_Apellidos`, `Celular`, `email`, `direccion`, `Fecha_Creacion`, `Salario`, `cargo_id`) VALUES
(1, 'Aida Nohemí', 'Zapet', '34264323', 'zzzskaav@gmail.com', 'Comitancillo, San Marcos', '2019-10-17 05:34:31.127816', 1234.65, 1),
(2, 'Alejandro David', 'Coronado Gabriel', '3426431342', 'poadgf@gmail.com', 'Taltimiche, Comitancillo, San Marcos', '2019-10-17 05:38:19.378898', 800.75, 2),
(3, 'Víctor Hugo', 'Morales Pérez', '1235164765', 'qerssh@hotmail.com', 'San Pedro Sacatepéquez', '2019-10-17 08:53:06.943832', 234.65, 5),
(4, 'José', 'Cardenas', '134567845', 'zzzskaav@gmail.com', 'San Pedro Sacatepéquez', '2019-11-02 22:41:37.604426', 345, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transac_estudiantes`
--

CREATE TABLE `transac_estudiantes` (
  `id` int(11) NOT NULL,
  `Fecha_Transaccion` datetime(6) NOT NULL,
  `CantidadTotal` double NOT NULL,
  `Descripcion` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `estudiantes_id_estudiante_id` int(11) NOT NULL,
  `personal_id_personal_id` int(11) NOT NULL,
  `tutores_id_tutor_id` int(11) NOT NULL,
  `colegiaturas_id_mes_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `transac_estudiantes`
--

INSERT INTO `transac_estudiantes` (`id`, `Fecha_Transaccion`, `CantidadTotal`, `Descripcion`, `estudiantes_id_estudiante_id`, `personal_id_personal_id`, `tutores_id_tutor_id`, `colegiaturas_id_mes_id`) VALUES
(1, '2019-10-24 16:10:33.120958', 145.75, 'Costo por su inscripción del estudiante en el Grado de Primero Básico', 1, 1, 1, 1),
(2, '2019-11-02 22:48:03.290899', 345, 'Original', 3, 2, 3, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tutores`
--

CREATE TABLE `tutores` (
  `id` int(11) NOT NULL,
  `DPI_Tutor` varchar(14) COLLATE latin1_spanish_ci NOT NULL,
  `Nombres_Tutor` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `Apellidos_Tutor` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `Telefono_Tutor` varchar(8) COLLATE latin1_spanish_ci DEFAULT NULL,
  `Direccion_Tutor` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `email_Tutor` varchar(45) COLLATE latin1_spanish_ci DEFAULT NULL,
  `Fecha_Inscripcion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `tutores`
--

INSERT INTO `tutores` (`id`, `DPI_Tutor`, `Nombres_Tutor`, `Apellidos_Tutor`, `Telefono_Tutor`, `Direccion_Tutor`, `email_Tutor`, `Fecha_Inscripcion`) VALUES
(1, '12340157398105', 'Sergio Marco Tulio', 'Salvador Cabrera', '14325631', 'La Gomera, Tuichilupe, San Marcos', 'damiandra@hotmail.com', '2019-10-17 18:26:57.848595'),
(2, '1329987874', 'Carlos Humberto', 'López Tomás', '12345655', 'Taltimiche, Comitancillo, San Marcos', NULL, '2019-10-28 18:15:50.423064'),
(3, '12340157398105', 'Santos', 'Andrade', '1432563', 'Tuichilupe, San Marcos', 'damra@hotmail.com', '2019-11-02 22:45:56.597058');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `accesos`
--
ALTER TABLE `accesos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `accesos_personal_id_personal_id_db8892d0_fk_personal_id` (`personal_id_personal_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `carreras`
--
ALTER TABLE `carreras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `carreras_nivele_educativo_id__72377af6_fk_niveles_e` (`nivele_educativo_id_nivel_id`);

--
-- Indices de la tabla `carreras_grados`
--
ALTER TABLE `carreras_grados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `carreras_grados_carreras_id_carrera_id_7efac165_fk_carreras_id` (`carreras_id_carrera_id`),
  ADD KEY `carreras_grados_grados_id_grado_id_314b422b_fk_grados_id` (`grados_id_grado_id`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cursos_personal_id_personal_id_16f9ebbc_fk_personal_id` (`personal_id_personal_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `estudiantes_tutores_id_tutor_id_3a34f08d_fk_tutores_id` (`tutores_id_tutor_id`);

--
-- Indices de la tabla `estudiante_curso`
--
ALTER TABLE `estudiante_curso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `estudiante_curso_cursos_id_curso_id_3fb2c6aa_fk_cursos_id` (`cursos_id_curso_id`),
  ADD KEY `estudiante_curso_estudiantes_id_estud_e3150eb3_fk_estudiant` (`estudiantes_id_estudiante_id`);

--
-- Indices de la tabla `grados`
--
ALTER TABLE `grados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `grados_cursos`
--
ALTER TABLE `grados_cursos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `grados_cursos_cursos_id_curso_id_2902d77a_fk_cursos_id` (`cursos_id_curso_id`),
  ADD KEY `grados_cursos_grados_id_grado_id_105cfcd7_fk_grados_id` (`grados_id_grado_id`);

--
-- Indices de la tabla `meses_colegiaturas`
--
ALTER TABLE `meses_colegiaturas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `niveles_educativos`
--
ALTER TABLE `niveles_educativos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notas_cursos_id_curso_id_e0863edc_fk_cursos_id` (`cursos_id_curso_id`),
  ADD KEY `notas_estudiantes_id_estudiante_id_92fa3586_fk_estudiantes_id` (`estudiantes_id_estudiante_id`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `personal_cargo_id_9b1a9838_fk_cargos_id` (`cargo_id`);

--
-- Indices de la tabla `transac_estudiantes`
--
ALTER TABLE `transac_estudiantes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `transac_estudiantes_estudiantes_id_estud_e71a687f_fk_estudiant` (`estudiantes_id_estudiante_id`),
  ADD KEY `transac_estudiantes_personal_id_personal_3e18f1f4_fk_personal_` (`personal_id_personal_id`),
  ADD KEY `transac_estudiantes_tutores_id_tutor_id_2102981c_fk_tutores_id` (`tutores_id_tutor_id`),
  ADD KEY `transac_estudiantes_colegiaturas_id_mes__fc3aa7c4_fk_meses_col` (`colegiaturas_id_mes_id`);

--
-- Indices de la tabla `tutores`
--
ALTER TABLE `tutores`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `accesos`
--
ALTER TABLE `accesos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cargos`
--
ALTER TABLE `cargos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `carreras`
--
ALTER TABLE `carreras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `carreras_grados`
--
ALTER TABLE `carreras_grados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `estudiante_curso`
--
ALTER TABLE `estudiante_curso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `grados`
--
ALTER TABLE `grados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `grados_cursos`
--
ALTER TABLE `grados_cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `meses_colegiaturas`
--
ALTER TABLE `meses_colegiaturas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `niveles_educativos`
--
ALTER TABLE `niveles_educativos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `notas`
--
ALTER TABLE `notas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `personal`
--
ALTER TABLE `personal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `transac_estudiantes`
--
ALTER TABLE `transac_estudiantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tutores`
--
ALTER TABLE `tutores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `accesos`
--
ALTER TABLE `accesos`
  ADD CONSTRAINT `accesos_personal_id_personal_id_db8892d0_fk_personal_id` FOREIGN KEY (`personal_id_personal_id`) REFERENCES `personal` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `carreras`
--
ALTER TABLE `carreras`
  ADD CONSTRAINT `carreras_nivele_educativo_id__72377af6_fk_niveles_e` FOREIGN KEY (`nivele_educativo_id_nivel_id`) REFERENCES `niveles_educativos` (`id`);

--
-- Filtros para la tabla `carreras_grados`
--
ALTER TABLE `carreras_grados`
  ADD CONSTRAINT `carreras_grados_carreras_id_carrera_id_7efac165_fk_carreras_id` FOREIGN KEY (`carreras_id_carrera_id`) REFERENCES `carreras` (`id`),
  ADD CONSTRAINT `carreras_grados_grados_id_grado_id_314b422b_fk_grados_id` FOREIGN KEY (`grados_id_grado_id`) REFERENCES `grados` (`id`);

--
-- Filtros para la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `cursos_personal_id_personal_id_16f9ebbc_fk_personal_id` FOREIGN KEY (`personal_id_personal_id`) REFERENCES `personal` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `estudiantes_tutores_id_tutor_id_3a34f08d_fk_tutores_id` FOREIGN KEY (`tutores_id_tutor_id`) REFERENCES `tutores` (`id`);

--
-- Filtros para la tabla `estudiante_curso`
--
ALTER TABLE `estudiante_curso`
  ADD CONSTRAINT `estudiante_curso_cursos_id_curso_id_3fb2c6aa_fk_cursos_id` FOREIGN KEY (`cursos_id_curso_id`) REFERENCES `cursos` (`id`),
  ADD CONSTRAINT `estudiante_curso_estudiantes_id_estud_e3150eb3_fk_estudiant` FOREIGN KEY (`estudiantes_id_estudiante_id`) REFERENCES `estudiantes` (`id`);

--
-- Filtros para la tabla `grados_cursos`
--
ALTER TABLE `grados_cursos`
  ADD CONSTRAINT `grados_cursos_cursos_id_curso_id_2902d77a_fk_cursos_id` FOREIGN KEY (`cursos_id_curso_id`) REFERENCES `cursos` (`id`),
  ADD CONSTRAINT `grados_cursos_grados_id_grado_id_105cfcd7_fk_grados_id` FOREIGN KEY (`grados_id_grado_id`) REFERENCES `grados` (`id`);

--
-- Filtros para la tabla `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_cursos_id_curso_id_e0863edc_fk_cursos_id` FOREIGN KEY (`cursos_id_curso_id`) REFERENCES `cursos` (`id`),
  ADD CONSTRAINT `notas_estudiantes_id_estudiante_id_92fa3586_fk_estudiantes_id` FOREIGN KEY (`estudiantes_id_estudiante_id`) REFERENCES `estudiantes` (`id`);

--
-- Filtros para la tabla `personal`
--
ALTER TABLE `personal`
  ADD CONSTRAINT `personal_cargo_id_9b1a9838_fk_cargos_id` FOREIGN KEY (`cargo_id`) REFERENCES `cargos` (`id`);

--
-- Filtros para la tabla `transac_estudiantes`
--
ALTER TABLE `transac_estudiantes`
  ADD CONSTRAINT `transac_estudiantes_colegiaturas_id_mes__fc3aa7c4_fk_meses_col` FOREIGN KEY (`colegiaturas_id_mes_id`) REFERENCES `meses_colegiaturas` (`id`),
  ADD CONSTRAINT `transac_estudiantes_estudiantes_id_estud_e71a687f_fk_estudiant` FOREIGN KEY (`estudiantes_id_estudiante_id`) REFERENCES `estudiantes` (`id`),
  ADD CONSTRAINT `transac_estudiantes_personal_id_personal_3e18f1f4_fk_personal_` FOREIGN KEY (`personal_id_personal_id`) REFERENCES `personal` (`id`),
  ADD CONSTRAINT `transac_estudiantes_tutores_id_tutor_id_2102981c_fk_tutores_id` FOREIGN KEY (`tutores_id_tutor_id`) REFERENCES `tutores` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
