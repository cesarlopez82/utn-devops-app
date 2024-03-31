# Imagen oficial de Python como base
FROM python:3.9-slim

# Se define el directorio de trabajo en el contenedor
WORKDIR /app

# Se copia el archivo requirements.txt al directorio de trabajo
COPY configs/python/requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Se copia el código fuente de la aplicación al directorio de trabajo en el contenedor
COPY ../app.py .

# Se expone el puerto 8000 (o el puerto que tu aplicación usa)
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "app.py"]
