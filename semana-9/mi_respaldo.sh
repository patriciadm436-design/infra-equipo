#!/usr/bin/env bash
set -euo pipefail
DESTINO=/home/patty/respaldos
mkdir -p "$DESTINO"
tar -czf "$DESTINO/docs-$(date +%F).tar.gz" -C /home/patty documentos
echo "Respaldo creado con éxito: $(date +%F)"
