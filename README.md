# 📦 Sistema de Gestión Logística (Smart Inventory API)

> **API RESTful escalable para la gestión automatizada de inventarios, optimización de almacenamiento y trazabilidad de stock en tiempo real.**

---

## 📋 Descripción del Proyecto
Este sistema es una solución Backend diseñada para resolver problemas críticos de logística: el cálculo erróneo de espacios de almacenamiento y la inconsistencia en el stock.

A diferencia de un CRUD tradicional, este sistema implementa **lógica de negocio inteligente** directamente en el modelo de datos, garantizando que el inventario refleje siempre la realidad operativa mediante transacciones auditables.

## 🚀 Stack Tecnológico

| Tecnología | Uso en el Proyecto |
|------------|-------------------|
| **Python 3.12** | Lenguaje base optimizado. |
| **Django 5 & DRF** | Framework para construcción de API REST robusta. |
| **PostgreSQL** | Base de datos relacional para integridad de datos. |
| **Docker & Compose** | Contenerización para despliegue agnóstico (Infraestructura como Código). |
| **JWT (SimpleJWT)** | Seguridad basada en Tokens (Access/Refresh) estándar de la industria. |
| **Swagger / OpenAPI** | Documentación automática e interactiva. |

## ⚙️ Funcionalidades Core (Lógica de Negocio)

### 1. 📐 Cálculo Automático de Volumen (`Smart Calculation`)
El sistema elimina el error humano en la carga de datos.
* **Input:** El usuario ingresa dimensiones (`largo`, `ancho`, `alto`) en cm.
* **Proceso:** El modelo calcula automáticamente el volumen en metros cúbicos (`m³`) antes de guardar.
* **Uso:** Permite reportes precisos de ocupación de depósito.

### 2. 🔄 Control de Stock por Movimientos (`Audit Trail`)
El campo `stock_actual` **no es editable manualmente**.
* El stock se calcula dinámicamente: `∑ Entradas - ∑ Salidas`.
* Esto garantiza trazabilidad total: cada cambio en el stock tiene una fecha, hora y motivo asociado.

### 3. 🔒 Seguridad Bancaria (JWT)
API cerrada por defecto. Implementa el estándar **Bearer Token**:
* **Login:** Genera par de llaves (Access + Refresh).
* **Protección:** Middleware que rechaza peticiones anónimas (`401 Unauthorized`).

---

## 🛠️ Instalación y Despliegue Local

El proyecto está 100% Dockerizado. No requiere instalar Python ni PostgreSQL en la máquina local.

**1. Clonar el repositorio:**
```bash
git clone [https://github.com/TU_USUARIO/sistema_logistica.git](https://github.com/TU_USUARIO/sistema_logistica.git)
cd sistema_logistica
2. Iniciar servicios (Build & Run):

Bash

docker compose up --build
3. Acceder al sistema:

Documentación API (Swagger): http://localhost:8000/swagger/

Panel Administrativo: http://localhost:8000/admin/

🧪 Guía de Uso Rápida (Endpoints)
Paso 1: Autenticación
Enviar credenciales para obtener el Token.

POST /api/token/

Body: {"username": "admin", "password": "..."}

Paso 2: Crear Producto
POST /api/productos/

Header: Authorization: Bearer <TU_TOKEN>

Nota: Al enviar las dimensiones, el sistema devolverá el volumen_m3 calculado.

Paso 3: Cargar Stock (Entrada)
POST /api/movimientos/

Body: {"producto": 1, "cantidad": 50, "tipo": "ENTRADA"}

Resultado: El stock del producto 1 aumentará automáticamente.

👤 Autor
[TU NOMBRE] - Backend Developer

LinkedIn

Portfolio

Este proyecto fue desarrollado bajo estándares de arquitectura limpia y buenas prácticas de desarrollo backend.