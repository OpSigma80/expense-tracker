 ¡Listo! He creado un README.md completo para tu proyecto. 📄

Este documento incluye:

✅ **Descripción completa** del proyecto
✅ **Características** principales
✅ **Estructura** del proyecto explicada
✅ **Guía de instalación** paso a paso
✅ **Todos los comandos** necesarios
✅ **Instrucciones de uso**
✅ **Solución de problemas** comunes
✅ **Comandos de testing**
✅ **Información de los modelos**

# 💰 Python Expense Tracker

Una aplicación web desarrollada con Django para rastrear y gestionar gastos personales de manera sencilla y eficiente.

## 📋 Descripción

**Expense Tracker** es una herramienta de gestión financiera personal que te permite registrar, categorizar y analizar tus gastos diarios. La aplicación proporciona una interfaz intuitiva para llevar un control detallado de tus finanzas personales.

## ✨ Características

- 📝 **Registro de gastos**: Añade gastos con monto, categoría, fecha y descripción
- 👤 **Perfiles de usuario**: Cada usuario tiene su propio perfil con balance personalizado
- 📊 **Seguimiento de balance**: Visualiza tu balance actual en tiempo real
- 🏷️ **Categorización**: Organiza tus gastos por categorías
- 🔐 **Sistema de autenticación**: Registro e inicio de sesión seguro
- 📱 **Interfaz responsive**: Diseño adaptable a diferentes dispositivos

## 🛠️ Tecnologías

- **Backend**: Django 4.2.11
- **Base de datos**: SQLite3
- **Frontend**: HTML, CSS (templates Django)
- **Python**: 3.10 / 3.12

## 📁 Estructura del Proyecto

```
Python-Expense-tracker-master/
│
├── home/                      # App principal
│   ├── migrations/            # Migraciones de base de datos
│   ├── templates/             # Templates HTML
│   │   ├── base.html         # Template base
│   │   └── home.html         # Página principal
│   ├── admin.py              # Configuración del admin
│   ├── models.py             # Modelos (Profile, Expense)
│   ├── views.py              # Vistas
│   ├── urls.py               # URLs de la app
│   └── tests.py              # Tests unitarios
│
├── project/                   # Configuración del proyecto
│   ├── settings.py           # Configuración Django
│   ├── urls.py               # URLs principales
│   └── wsgi.py               # WSGI config
│
├── static/                    # Archivos estáticos (CSS, JS, imágenes)
├── db.sqlite3                # Base de datos SQLite
├── manage.py                 # Script de gestión Django
└── requirements.txt          # Dependencias del proyecto
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Anaconda (opcional, pero recomendado)

### Paso 1: Clonar o descargar el repositorio

```bash
cd C:\Users\rovir\Python-Expense-tracker-master
```

### Paso 2: Crear entorno virtual (con Anaconda)

```bash
conda create -n Avanzado python=3.10
conda activate Avanzado
```

O con venv:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Aplicar migraciones

```bash
python manage.py migrate
```

### Paso 5: Crear superusuario (admin)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu cuenta de administrador.

### Paso 6: Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 🎮 Uso

### Acceso a la aplicación

1. **Página principal**: `http://127.0.0.1:8000/`
2. **Panel de administración**: `http://127.0.0.1:8000/admin/`

### Funcionalidades principales

1. **Registrar un gasto**:
   - Ingresa el monto
   - Selecciona o crea una categoría
   - Añade una descripción
   - Guarda el registro

2. **Ver tu balance**:
   - El balance se actualiza automáticamente
   - Visualiza tus gastos totales

3. **Gestionar gastos**:
   - Edita gastos existentes
   - Elimina registros
   - Filtra por fecha o categoría

## 🧪 Testing

Ejecutar todas las pruebas:

```bash
python manage.py test
```

Ejecutar tests con cobertura:

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera reporte HTML
```

Resultados esperados:
```
Found 6 test(s).
Creating test database for alias 'default'...
......
Ran 6 tests in 7.842s
OK
```

## 📊 Modelos de Datos

### Profile (Perfil de Usuario)
- `user`: Usuario de Django (OneToOne)
- `balance`: Balance actual del usuario
- `expense`: Gastos totales acumulados

### Expense (Gasto)
- `user`: Usuario que registró el gasto
- `amount`: Monto del gasto
- `category`: Categoría del gasto
- `description`: Descripción opcional
- `date`: Fecha del gasto

## 🔧 Comandos Útiles

### Gestión del proyecto

```bash
# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver

# Ejecutar servidor en puerto específico
python manage.py runserver 8080

# Ejecutar shell de Django
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic
```

### Testing

```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests de una app específica
python manage.py test home

# Ejecutar test específico
python manage.py test home.tests.TestClassName
```

### Base de datos

```bash
# Crear backup de la base de datos
copy db.sqlite3 db_backup.sqlite3

# Ver estructura de la base de datos
python manage.py dbshell
```

## 🐛 Solución de Problemas

### Error: "Requested setting INSTALLED_APPS, but settings are not configured"

**Solución**: Usa `python manage.py test` en lugar de `python tests.py`

### Error: Puerto en uso

**Solución**: 
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# O usa otro puerto
python manage.py runserver 8080
```

### Error de migraciones

**Solución**:
```bash
python manage.py migrate --run-syncdb
```

## 📝 Notas Adicionales

- La base de datos SQLite (`db.sqlite3`) contiene todos los datos
- Los archivos estáticos deben estar en la carpeta `static/`
- Los templates HTML están en `home/templates/`
- El proyecto usa Django 4.2.11 (LTS)

## 📄 Licencia

Este proyecto está bajo la licencia especificada en el archivo `LICENCE`.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añade nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📞 Soporte

Si encuentras algún problema o tienes preguntas:
- Revisa la sección de solución de problemas
- Verifica que todas las dependencias estén instaladas
- Asegúrate de estar usando el entorno virtual correcto

---

**Desarrollado con ❤️ usando Django**

*Última actualización: Enero 2026*


