# 🏪 Sistema de Gestión de Ventas y Stock

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

Sistema web completo para la **gestión de ventas, control de inventario y registro de clientes**, desarrollado con **Django** y **Python**. Incluye autenticación de usuarios, roles y permisos, cálculo automático de IGV (18%) y gestión de stock en tiempo real.

---

## 📸 Capturas de Pantalla

### 🔐 Pantalla de Inicio de Sesión
<img width="541" height="703" alt="image" src="https://github.com/user-attachments/assets/bc7c4ebf-23ad-4013-abf5-823c201898fd" />


### 🏠 Panel Principal (Dashboard)
<img width="1901" height="572" alt="image" src="https://github.com/user-attachments/assets/366a4666-6914-46bb-b2fd-b782ad814ea8" />


### 👥 Gestión de Clientes (CRUD)
<img width="1907" height="529" alt="image" src="https://github.com/user-attachments/assets/eb1d2341-8a10-4631-a947-a7e9aa513fc2" />


### 📦 Gestión de Productos (CRUD)
<img width="767" height="611" alt="image" src="https://github.com/user-attachments/assets/bb1d150e-5857-4e64-9a8d-6c4f7738a4d1" />


### 💰 Gestión de Ventas
<img width="766" height="591" alt="image" src="https://github.com/user-attachments/assets/c801f80d-d654-453e-9bbb-be33027d9164" />


---

## ✨ Características Principales

*   🔐 **Autenticación y Autorización:** Sistema de login con roles (Administrador, Usuario) y permisos granulares por grupo.
*   👥 **CRUD de Clientes:** Registro, consulta, modificación y eliminación de clientes con validación de DNI único (8 dígitos).
*   📦 **CRUD de Productos:** Gestión de inventario con control de stock, precios, fechas de vencimiento y estado (activo/inactivo).
*   💰 **Gestión de Ventas:** Registro de ventas con cálculo automático de subtotal, IGV (18%) y total. Actualización automática del stock.
*   📊 **Dashboard Interactivo:** Panel principal con acceso rápido a todas las funcionalidades según los permisos del usuario.
*   📱 **Diseño Responsive:** Interfaz adaptable a dispositivos móviles, tablets y escritorio.
*   🔄 **Anulación de Ventas:** Las ventas se anulan (no se eliminan) y el stock se restaura automáticamente.
*   📈 **Reportes Estadísticos:** Totales de ventas, IGV recaudado y conteo de registros en tiempo real.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
| :--- | :--- |
| **Python 3.14** | Lenguaje de programación principal |
| **Django 6.1** | Framework web backend |
| **SQLite** | Base de datos relacional (desarrollo) |
| **HTML5 / CSS3** | Estructura y estilos del frontend |
| **JavaScript** | Interactividad (AJAX, cálculo de totales, modales) |
| **Django ORM** | Gestión de la base de datos |
| **Django Auth** | Autenticación y permisos |

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
│ │ ├── autenticacion/ # Login, Home
│ │ ├── clientes/ # CRUD Clientes
│ │ ├── productos/ # CRUD Productos
│ │ └── ventas_simples/ # CRUD Ventas
│ ├── admin.py # Configuración del panel admin
│ ├── forms.py # Formularios Django
│ ├── middleware.py # Middleware personalizado
│ ├── models.py # Modelos de datos
│ ├── urls.py # URLs de la app
│ └── views.py # Lógica de negocio
│
├── requirements.txt # Dependencias del proyecto
├── manage.py # Utilidad de Django
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
admin	1234567A	Administrador
