# infra-equipo

Repositorio de infraestructura del laboratorio de Administración de Centros de Cómputo.

## Descripción
Despliegue con Docker Compose de Nginx, MySQL y HAProxy con red propia y volumen persistente correspondiente a la Semana 7.

## Requisitos
- Debian 13 con Docker y el complemento Docker Compose v2.
- Archivo .env creado a partir de .env.ejemplo, con las contraseñas de la base de datos (no se sube al repositorio por seguridad).

## Flujo de Trabajo (Semana 8)
- Uso estricto de Git Flow con ramas separadas (`main` y `desarrollo-patty`).
- Fusión formal mediante estrategia de historial gráfico (`--no-ff`).
