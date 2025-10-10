# 🌐 Proyecto Portafolio Web – Django (v5.2.5)

**Autor:** Diego Sandoval Olguín  
**Carrera:** Analista Programador  
**Institución:** INACAP  
**Asignatura:** Programación Back-End  

---

## ✅ Despliegue en Railway (paso a paso)
1️⃣ **Crear proyecto en Railway:**  
   - `New Project` ➜ **Deploy from GitHub** (conecta tu repositorio).  
2️⃣ **Agregar plugin de base de datos:**  
   - `Plugins` ➜ **Add PostgreSQL** (Railway crea automáticamente la variable `DATABASE_URL`).  
3️⃣ **Configurar Variables de entorno:**  
   - `DEBUG=False`  
   - `SECRET_KEY=(clave secreta generada)`  
   - `ALLOWED_HOSTS=web-production-83fc.up.railway.app,localhost,127.0.0.1`  
4️⃣ **Verificar el comando de inicio:**  
   - En `Settings`, asegúrate de que el **Start Command** sea:  
     ```
     gunicorn miportafolio.wsgi
     ```
     *(El Procfile ya lo define correctamente)*  
5️⃣ **Ejecutar comandos iniciales (desde Shell o CLI):**  
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
6️⃣ Abrir la URL pública y verificar funcionamiento:
👉 https://web-production-83fc.up.railway.app

📘 Descripción General
Este proyecto corresponde a un portafolio web personal desarrollado con el framework Django, como parte de la asignatura Programación Back-End.
La aplicación incluye funcionalidades CRUD completas, manejo de plantillas, rutas dinámicas y despliegue tanto en un entorno de desarrollo local como en producción con Railway.

⚙️ Tecnologías Aplicadas
Lenguaje principal: Python

Framework web: Django

Base de datos local: SQLite3

Servidor de desarrollo: Django runserver

Gestor de dependencias: pip

Entorno virtual: venv

Despliegue en producción: Railway

Control de versiones: Git y GitHub

🧩 Funcionalidades Principales
✅ CRUD completo (crear, leer, actualizar y eliminar registros).
✅ Plantillas HTML dinámicas con Django Template Language.
✅ Manejo de archivos estáticos (CSS, imágenes, JS).
✅ Estructura modular con la aplicación “proyectos”.
✅ Sistema de autenticación (inicio y cierre de sesión).
✅ Configuración lista para despliegue en Railway.

🚀 Instrucciones para ejecutar el proyecto localmente
1️⃣ Clonar el repositorio desde GitHub:

bash
Copiar código
git clone https://github.com/diegolguin/miportafolio_pro_v2.git
2️⃣ Entrar a la carpeta del proyecto:

bash
Copiar código
cd miportafolio_pro_v2
3️⃣ Crear y activar el entorno virtual (Windows):

bash
Copiar código
python -m venv venv
venv\Scripts\activate
4️⃣ Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
5️⃣ Ejecutar el servidor local:

bash
Copiar código
python manage.py runserver
6️⃣ Abrir en el navegador:
👉 http://127.0.0.1:8000/



🌍 Proyecto en Producción
🔗 Sitio desplegado en Railway:
👉 https://web-production-83fc.up.railway.app