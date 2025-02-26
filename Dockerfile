# Usa una imagen base que tiene herramientas de red y evita problemas de DNS
FROM python:3.11

# Configurar el directorio de trabajo
WORKDIR /app

# Configurar DNS manualmente para evitar problemas de conexión


# Actualizar repositorios y asegurarse de que las dependencias estén instaladas
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev iputils-ping curl \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Actualizar pip y herramientas de instalación
RUN pip install --upgrade pip setuptools wheel

# Copiar el archivo de dependencias
COPY requirements.txt requirements.txt

# Instalar las dependencias de Python (incluyendo psycopg2-binary)
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copiar el código fuente
COPY src/ src/

# Exponer el puerto de la aplicación
EXPOSE 5000

# Variables de entorno de la base de datos
ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_HOST=localhost
ENV DB_PORT=5432

# Comando para iniciar la aplicación
CMD ["python", "src/app.py"]
