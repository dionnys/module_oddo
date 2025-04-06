# Odoo 16 en Docker 🐳

Este proyecto permite desplegar una instancia de **Odoo 16** usando **Docker y Docker Compose**, junto con una base de datos PostgreSQL 13. Incluye configuración automática del sistema y permite cargar módulos personalizados.

---

## 🚀 Características

- Odoo 16 en contenedor Docker
- PostgreSQL 13 como base de datos
- Montaje de addons personalizados
- Inicialización automática de la base de datos `odoo`
- Configuración mediante `odoo.conf`
- Soporte para reinicio y reconstrucción del entorno

---

## ⚙️ Requisitos

- Docker instalado
- Docker Compose instalado
-  acceso a internet para dependencias externas

---

## 📦 Instalación

1. **Clonar el repositorio** (o copiar los archivos `docker-compose.yml`, `odoo.conf`, `env` y `addons/`):

```bash
git clone https://github.com/dionnys/module_oddo.git
cd module-movies
