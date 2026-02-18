
# API de Productos - DevOps Starter

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

---
## Introducción

Usaremos este proyecto como ejemplo real de un flujo DevOps. Tenemos una API con **FastAPI** conectada a **PostgreSQL**, corriendo dentro de **Docker** para evitar el típico "en mi máquina funciona". 

Pero lo más importante es la automatización: incluimos tests que **GitHub Actions** ejecuta por nosotros cada vez que subimos código a GitHub. Es nuestra red de seguridad: si una modificación introduce un error, el "robot" de GitHub nos avisará antes de que el problema pase a mayores.

---

## Estructura del Proyecto

```text
proyecto_final/
├── app/                # Todo el código de la API (FastAPI)
│   ├── main.py         # Punto de entrada
│   ├── database.py     # Configuración de SQLAlchemy
│   ├── models.py       # Tablas de la Base de Datos
│   └── schemas.py      # Validación con Pydantic
├── tests/              # Pruebas unitarias e integración
├── .github/workflows/  # Automatización (CI/CD) con GitHub Actions
├── Dockerfile          # Receta de la imagen de la API
├── docker-compose.yml  # Orquestador de servicios (API + DB)
├── requirements.txt    # Librerías necesarias
└── .env                # Variables de entorno (No subir a GitHub)
```
---
## Requisitos previos
Para poner esto en marcha necesitas:

1. Docker Desktop (instalado y corriendo).

2. Git para el control de versiones.

3. PyCharm (Recomendado como IDE).
---
## Inicio Rápido
1. Clona el proyecto y ábrelo en PyCharm.

2. Crea tu archivo de configuración:
Crea un archivo .env en la raíz y añade tus credenciales (ejemplo):
```
DATABASE_URL=postgresql://tu_usuario:tu_password@db:5432/productos
```
3. Levanta el sistema con Docker:
Abre la terminal de PyCharm y ejecuta:
```
docker-compose up --build
```
4. Prueba la API:
Entra en http://localhost:8000/docs para ver el Swagger interactivo.
---
## Testing y Calidad
Para ejecutar los tests manualmente dentro del contenedor:
```
docker-compose exec api pytest -p no:cacheprovider tests/
```
## Integración Continua (CI)
Al subir el código a GitHub, el archivo .github/workflows/ci.yml se activará automáticamente:

1. Levanta una base de datos PostgreSQL temporal.

2. Instala las dependencias.

3. Ejecuta la batería de tests.

4. Si todo está verde, el código es seguro.
---
## Flujo de trabajo con PyCharm
Este proyecto está optimizado para trabajar con PyCharm:

* **Subidas a GitHub**: No necesitas comandos de consola. Usa la pestaña "Commit" (Ctrl+K), escribe tu mensaje y selecciona "Commit and Push". GitHub Actions se encargará del resto.

* **Docker Integration**: Puedes gestionar tus contenedores directamente desde la pestaña "Services" en la parte inferior de PyCharm.

* **Base de Datos**: Puedes conectar el panel "Database" de PyCharm a localhost:5432 para ver tus tablas en tiempo real.
---
## Tecnologías Utilizadas
* **FastAPI**: Framework moderno de alto rendimiento.

* **PostgreSQL**: Base de datos relacional robusta.

* **SQLAlchemy**: ORM para gestión de datos.

* **Pydantic**: Validación de esquemas.

* **Docker & Compose**: Contenerización y orquestación.

* **Pytest**: Pruebas automáticas.

