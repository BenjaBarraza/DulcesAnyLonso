# 🍰 Dulces Anylonso

### Plataforma Web para Pastelería Artesanal

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge\&logo=docker)
![JavaScript](https://img.shields.io/badge/Frontend-JavaScript%20%26%20CSS3-orange?style=for-the-badge)
![Jazzmin](https://img.shields.io/badge/Admin-Jazzmin-crimson?style=for-the-badge)

**Dulces Anylonso** es una plataforma web diseñada para una pastelería artesanal en Santiago de Chile. Permite explorar productos, cotizar pedidos personalizados y gestionar solicitudes por WhatsApp o correo, todo mediante una interfaz rápida y responsiva.

---

## ✨ Características Principales

### 🛍️ Frontend (Experiencia del Cliente)

* Catálogo interactivo con filtrado dinámico.
* Vista rápida mediante modales con imagen, precio y detalles.
* Carrito de cotización con almacenamiento en *LocalStorage*.
* Envío automático del pedido por WhatsApp.
* Sistema de testimonios administrable desde Django.
* Diseño responsive y optimizado.

---

### ⚙️ Backend (Gestión y Lógica)

* Modelos: **Torta**, **Categoría**, **Testimonio**.
* Admin profesionalizado con **Jazzmin** (temas, buscador, iconos).
* Formulario de contacto con plantilla HTML y SMTP.
* Variables de entorno mediante `.env`.
* Preparado para producción con Gunicorn + Docker.

---

## 🛠️ Tecnologías Utilizadas

| Componente      | Tecnología                     |
| --------------- | ------------------------------ |
| Backend         | Django 5+                      |
| Lenguaje        | Python 3.10                    |
| Frontend        | HTML5, CSS3, JavaScript        |
| Base de Datos   | SQLite3                        |
| Contenedores    | Docker + Docker Compose        |
| Librerías clave | Pillow, Jazzmin, python-dotenv |

---

## 🚀 Instalación

### 🔧 Requisitos previos

* Docker Desktop *(Recomendado)*
* O bien: Python 3.10+ y Git

---

## 🐳 Instalación con Docker (Recomendada)

```bash
git clone https://github.com/tu-usuario/dulcesanylonso.git
cd dulcesanylonso
docker-compose up --build
```

Acceso a la app:

* **Web:** [http://localhost:8000](http://localhost:8000)
* **Admin:** [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 📝 Configuración del Archivo `.env`

Crea un archivo `.env` en la raíz del proyecto:

```ini
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# SMTP Gmail
EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_app
```

---

## 🐍 Instalación Manual (Sin Docker)

```bash
python -m venv venv
# Windows
env\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Migraciones:

```bash
python manage.py migrate
```

Crear superusuario:

```bash
python manage.py createsuperuser
```

Ejecutar servidor:

```bash
python manage.py runserver
```

---

## 📁 Estructura del Proyecto

```
dulcesanylonso/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── manage.py
├── dulcesanylonso/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── web/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── static/web/
│   │   ├── css/style.css
│   │   └── js/script.js
│   └── templates/web/index.html
├── correo/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
└── media/
```

---

## ❤️ Créditos

Proyecto creado para la pastelería **Dulces Anylonso**, digitalizando su catálogo y proceso de cotizaciones.

---

## 📩 Contacto

Para mejoras o dudas puedes abrir un issue o contribuir directamente al repositorio.
