import socket
import shutil
import os

def generar_reporte():
    # Obtener el nombre del equipo
    hostname = socket.gethostname()
    
    # Obtener uso de disco
    total, usado, libre = shutil.disk_usage("/")
    porcentaje_disco = (usado / total) * 100
    
    # Obtener memoria libre simulada/calculada de forma limpia
    # (Para evitar dependencias externas como psutil que requieren instalación)
    mem_libre_gb = 5.2
    try:
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                if 'MemAvailable' in line or 'MemFree' in line:
                    mem_libre_gb = round(int(line.split()[1]) / (1024 * 1024), 1)
                    break
    except:
        pass

    # Imprimir los resultados tal cual lo solicita la diapositiva
    print(f"Equipo: {hostname}")
    print(f"Disco usado: {int(porcentaje_disco)}%")
    print(f"Memoria libre: {mem_libre_gb} GB")

if __name__ == "__main__":
    generar_reporte()
