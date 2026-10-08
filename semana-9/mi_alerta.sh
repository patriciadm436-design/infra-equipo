#!/usr/bin/env bash
USO=$(df / --output=pcent | tail -1 | tr -dc '0-9')
[ "$USO" -ge 80 ] && echo "ALERTA: ${USO}%" || echo "Disco OK: ${USO}%"
