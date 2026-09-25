# 🏪 Sistema de Gestión de Ventas y Stock

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

Sistema web completo para la **gestión de ventas, control de inventario y registro de clientes**, desarrollado con **Django** y **Python**. Incluye autenticación de usuarios, roles y permisos, cálculo automático de IGV (18%), gestión de stock en tiempo real, exportación a Excel/PDF y **modo oscuro**.

---

## 📸 Capturas de Pantalla

### 🔐 Pantalla de Inicio de Sesión
<img width="1919" height="984" alt="image" src="https://github.com/user-attachments/assets/3c5e0eaa-2580-42f8-bb05-842fa81b3c94" />


### 🏠 Panel Principal (Dashboard)
<img width="1865" height="960" alt="image" src="https://github.com/user-attachments/assets/e6417b47-66e8-4fbd-91fb-76ba044489c3" />

### 👥 Gestión de Clientes (CRUD)
<img width="1909" height="716" alt="image" src="https://github.com/user-attachments/assets/57a84d51-8c2e-4767-97f1-751bb8724750" />


### 📦 Gestión de Productos (CRUD)
<img width="1757" height="477" alt="image" src="https://github.com/user-attachments/assets/69683154-81ff-4c45-99c6-34eebf8f8cbe" />


### 💰 Gestión de Ventas
<img width="1770" height="481" alt="image" src="https://github.com/user-attachments/assets/5c755778-1e9a-43fb-a5ef-efc1a6708469" />


### 🌙 Modo Oscuro
<img width="1895" height="597" alt="image" src="https://github.com/user-attachments/assets/7907602a-9a98-4e58-bacd-5a7cca169c0e" />


---

## ✨ Características Principales

*   🔐 **Autenticación y Autorización:** Sistema de login con roles (Administrador, Usuario) y permisos granulares por grupo.
*   👥 **CRUD de Clientes:** Registro, consulta, modificación y eliminación de clientes con validación de DNI único (8 dígitos).
*   📦 **CRUD de Productos:** Gestión de inventario con control de stock, precios, fechas de vencimiento y estado (activo/inactivo).
*   🔄 **Activar/Desactivar Productos:** Cambio de estado sin eliminar de la base de datos.
*   💰 **Gestión de Ventas:** Registro de ventas con cálculo automático de subtotal, IGV (18%) y total. Actualización automática del stock.
*   🔍 **Búsqueda de Ventas:** Modificar y anular ventas mediante búsqueda por código.
*   📊 **Dashboard Interactivo:** Panel principal con acceso rápido a todas las funcionalidades según los permisos del usuario.
*   📱 **Diseño Responsive:** Interfaz adaptable a dispositivos móviles, tablets y escritorio.
*   🔄 **Anulación de Ventas:** Las ventas se anulan (no se eliminan) y el stock se restaura automáticamente.
*   📈 **Reportes Estadísticos:** Totales de ventas, IGV recaudado y conteo de registros en tiempo real.
*   📊 **Exportación a Excel:** Descarga de listados en formato `.xlsx` con formato profesional.
*   📄 **Exportación a PDF:** Descarga de reportes en formato PDF con tablas y totales.
*   🌙 **Modo Oscuro:** Interfaz adaptable con tema claro/oscuro persistente.
*   🎨 **Diseño Moderno:** Interfaz limpia con gradientes, animaciones y tarjetas de gestión.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
| :--- | :--- |
| **Python 3.14** | Lenguaje de programación principal |
| **Django 6.1** | Framework web backend |
| **SQLite** | Base de datos relacional (desarrollo) |
| **HTML5 / CSS3** | Estructura y estilos del frontend |
| **JavaScript** | Interactividad (AJAX, cálculo de totales, modales, modo oscuro) |
| **Django ORM** | Gestión de la base de datos |
| **Django Auth** | Autenticación y permisos |
| **openpyxl** | Generación de archivos Excel |
| **ReportLab** | Generación de archivos PDF |

---

## 🏗️ Arquitectura del Proyecto
sistema-gestion-ventas/
│
├── miweb/ # Configuración principal del proyecto
│ ├── settings.py # Configuración global
│ ├── urls.py # URLs raíz
│ └── wsgi.py # Configuración WSGI
│
├── venta/ # Aplicación principal
│ ├── migrations/ # Migraciones de la BD
│ ├── templates/venta/ # Plantillas HTML
│ │ ├── base.html # Plantilla base (layout + modo oscuro)
│ │ ├── autenticacion/ # Login, Home
│ │ ├── clientes/ # CRUD Clientes
│ │ ├── productos/ # CRUD Productos
│ │ └── ventas_simples/ # CRUD Ventas
│ ├── views/ # Vistas organizadas por módulo
│ │ ├── init.py
│ │ ├── autenticacion_views.py
│ │ ├── clientes_views.py
│ │ ├── productos_views.py
│ │ ├── ventas_views.py
│ │ └── utils_views.py
│ ├── admin.py # Configuración del panel admin
│ ├── forms.py # Formularios Django
│ ├── middleware.py # Middleware personalizado
│ ├── models.py # Modelos de datos
│ ├── urls.py # URLs de la app
│ └── init.py
│
├── requirements.txt # Dependencias del proyecto
├── manage.py # Utilidad de Django
├── .gitignore # Archivos ignorados por Git
└── README.md # Este archivo


---

## 🚀 Instalación y Ejecución Local

Sigue estos pasos para ejecutar el proyecto en tu máquina:

### 1. Clonar el repositorio

```bash
git clone https://github.com/davidhuaman-2008/sistema-gestion-ventas.git
cd sistema-gestion-ventas

# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/

Usuario	Contraseña	Rol
admin	1234567A	Administrador

📁 Estructura de la Base de Datos
El sistema cuenta con los siguientes modelos:

Cliente: DNI, nombres, fecha de registro, fecha de sistema.

Producto: Código, nombre, descripción, precio, stock, fecha de vencimiento, estado (activo/inactivo), fecha de registro.

VentaSimple: Código, cliente, producto, cantidad, precio unitario, subtotal, IGV, total, fecha, estado (activa/anulada).

Venta / VentaDetalle: Modelos preparados para ventas complejas con múltiples productos.

🎨 Módulos del Sistema
👥 Clientes
Crear nuevo cliente con validación de DNI único.

Consultar listado completo de clientes.

Modificar datos de clientes existentes.

Eliminar clientes (con confirmación).

Exportar listado a Excel y PDF.

📦 Productos
Registrar nuevos productos con stock, precio y fecha de vencimiento.

Consultar listado de productos (activos e inactivos).

Modificar datos de productos.

Activar/Desactivar productos sin eliminarlos.

Eliminar productos definitivamente de la BD.

Ordenamiento por columnas (ascendente/descendente).

Exportar listado a Excel y PDF.

💰 Ventas
Registrar nuevas ventas con cálculo automático de IGV (18%).

Consultar listado de ventas (activas y anuladas).

Modificar ventas mediante búsqueda por código.

Anular ventas (restaura el stock automáticamente).

Exportar listado a Excel y PDF.

🎯 Próximas Mejoras
□ Reportes en PDF y Excel más detallados.
□ Gráficos estadísticos con Chart.js.
□ Integración con pasarelas de pago.
□ API REST con Django REST Framework.
□ Despliegue en producción con PostgreSQL y Docker.
□ Notificaciones por correo electrónico.
□ Sistema de roles y permisos más granular.
□ Búsqueda avanzada con filtros.
👨‍💻 Autor
David Efrain Huaman Romero

📧 Email: dhuaman.2008@gmail.com

💼 LinkedIn: linkedin.com/in/dhuaman2008

🌐 Portafolio: new-portfolio-beta-ochre.vercel.app

🐙 GitHub: github.com/davidhuaman-2008

📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

