
> ✅ **Despliegue en Railway (paso a paso)**
1) Crea proyecto en Railway ➜ **New Project** ➜ **Deploy from GitHub** (conecta tu repo).
2) **Plugins ➜ Add PostgreSQL** (Railway crea `DATABASE_URL` automáticamente).
3) En **Variables** agrega:
   - `DEBUG`=`False`
   - `SECRET_KEY`=`(genera una secreta)`
   - `ALLOWED_HOSTS`=`<tu-subdominio>.up.railway.app,localhost,127.0.0.1`
4) En **Settings** asegúrate que el **Start Command** sea: `gunicorn miportafolio.wsgi` (Procfile ya lo define).
5) **Deploy** y luego ejecuta en **Shell** (o desde CI) los comandos:
   - `python manage.py migrate`
   - `python manage.py collectstatic --noinput`
6) Abre el **Public URL** y verifica que carga sin errores.



# 🌐 Proyecto Portafolio Web - Django (Django 5.2.5)

**Autor:** Diego Sandoval Olguín  
**Carrera:** Analista Programador  
**Institución:** INACAP  
**Asignatura:** Programación Back-End  

---

## 📘 Descripción General

Este proyecto corresponde a un **portafolio web personal** desarrollado con el framework **Django**, como parte de la asignatura de *Programación Back-End*.

La aplicación incluye funcionalidades CRUD completas, manejo de plantillas, rutas dinámicas y despliegue en un entorno de desarrollo y producción.

---

## ⚙️ Tecnologías Aplicadas

- **Lenguaje principal:** Python  
- **Framework web:** Django  
- **Base de datos:** SQLite3  
- **Servidor de desarrollo:** Django runserver  
- **Gestor de dependencias:** pip  
- **Entorno virtual:** venv  
- **Despliegue:** Railway (configuración en progreso)  
- **Control de versiones:** Git y GitHub  

---

## 🧩 Funcionalidades principales

✅ Creación, lectura, actualización y eliminación de registros (**CRUD completo**).  
✅ Plantillas HTML dinámicas con Django Template Language.  
✅ Manejo de archivos estáticos (CSS, imágenes, JS).  
✅ Estructura modular (aplicación “proyectos”).  
✅ Sistema de autenticación con inicio y cierre de sesión.  
✅ Configuración para despliegue en **Railway**.  

---

## 🚀 Instrucciones para ejecutar el proyecto localmente

1. **Clonar el repositorio desde GitHub:**
   ```bash
   git clone https://github.com/diegolguin/miportafolio_pro_v2.git

Entrar a la carpeta del proyecto:

cd miportafolio_pro_v2


Crear y activar el entorno virtual (Windows):

python -m venv venv
venv\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar el servidor local:

python manage.py runserver


Abrir en el navegador:

http://127.0.0.1:8000/
Contacto

Autor: Diego Sandoval Olguín
Carrera: Analista Programador - INACAP