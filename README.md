

(Versión en Inglés)


# FinTrack Pro 🚀
**High-Performance Financial Management System**
![Dashboard] (https://github.com/OpSigma80/expense-tracker/blob/main/assets/Captura%20de%20pantalla%202026-01-28%20214820.png)

FinTrack Pro is not just a simple expense tracker; it is a robust web application built with **Django** that implements industry standards for financial data integrity and application security.

## 🛡️ Engineering Features (Steel Wall Architecture)

This project has been architected to meet professional software standards:

- **Event-Driven Architecture (Signals):** Balance calculations are decoupled from the views. Using `django.db.models.signals`, the system ensures user profiles are automatically updated whenever a transaction is created, modified, or deleted.
- **Financial Precision:** Strict use of `DecimalField` instead of floats to eliminate binary rounding errors, ensuring every cent is accounted for with 100% accuracy.
- **Security & Hardening:** - **Environment Management:** Secured sensitive data (Secret Keys, DB credentials) using `python-decouple`.
    - **Middleware Protection:** Built-in protection against XSS, CSRF, and Clickjacking.
    - **Multi-layer Validation:** Data integrity enforced at HTML5, Django Form, and Database levels.
- **Professional UX:** Real-time feedback using the Django Messaging Framework (`django.contrib.messages`) for seamless user interaction.

## 🛠️ Tech Stack

- **Backend:** Python 3.x / Django 4.2+
- **Database:** SQLite (Dev) / PostgreSQL Ready.
- **Frontend:** HTML5, CSS3 (Custom Minimalist UI with Google Fonts).
- **Security:** Python-Decouple, Dotenv.

## 🚀 Installation & Setup

1. **Clone the repository:**
 
   git clone [https://github.com/your-user/FinTrack-Pro.git](https://github.com/your-user/FinTrack-Pro.git)



2. **Environment Configuration:**
Create a `.env` file in the root directory:
env
SECRET_KEY=your_secure_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost



3. **Database Setup:**

python manage.py makemigrations
python manage.py migrate




4. **Run Server:**

python manage.py runserver


*Developed with a focus on scalability, data integrity, and security.*
__________________________________________________________________________________________________________________________________________________________________________________________
(version Español)
 FinTrack Pro 🚀
**Sistema de Gestión Financiera de Alto Rendimiento**

FinTrack Pro no es solo un seguidor de gastos; es una aplicación web robusta construida con **Django** que implementa estándares de industria para la integridad de datos financieros y seguridad de aplicaciones.

## 🛡️ Características de Ingeniería (Muro de Acero)

Este proyecto ha sido refactorizado para cumplir con estándares profesionales:

- **Arquitectura Basada en Eventos (Signals):** El cálculo de balances no se hace en la vista. Se utiliza `django.db.models.signals` para desacoplar la lógica de negocio, asegurando que el perfil del usuario se actualice automáticamente ante cualquier cambio en las transacciones.
- **Precisión Financiera:** Uso estricto de `DecimalField` en lugar de floats para evitar errores de redondeo binario, garantizando que cada centavo sea contabilizado correctamente.
- **Seguridad y Blindaje:** - Gestión de variables de entorno mediante `python-decouple` para proteger llaves secretas y credenciales.
    - Protección contra ataques XSS y CSRF configurada en el middleware.
    - Validación de tipos de datos en múltiples capas (HTML5, Django Forms y Nivel de Base de Datos).
- **UX Profesional:** Sistema de mensajería dinámica (`django.contrib.messages`) para feedback en tiempo real sobre el éxito o fallo de las operaciones.

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.x / Django 4.2+
- **Base de Datos:** SQLite (Desarrollo) / Compatible con PostgreSQL.
- **Frontend:** HTML5, CSS3 (Custom Design con Google Fonts).
- **Seguridad:** Python-Decouple, Dotenv.

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
  
   git clone [https://github.com/tu-usuario/Python-Expense-tracker-master.git](https://github.com/tu-usuario/Python-Expense-tracker-master.git)



2. **Configurar el entorno:**
Crea un archivo `.env` en la raíz con:

SECRET_KEY=tu_llave_secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost




3. **Ejecutar Migraciones:**

python manage.py makemigrations
python manage.py migrate




4. **Iniciar el servidor:**

python manage.py runserver


*Desarrollado con un enfoque en escalabilidad y seguridad de datos.*



