# Usa la imagen base de Python para Debian Buster slim
FROM python:3.8-slim-buster

#instalacion dependencias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todo el contenido del directorio actual al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el comando para iniciar la aplicación
CMD ["python", "count_people.py"]
