# Usar la imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos.
COPY requirements.txt /app
COPY app.py /app
COPY test_app.py /app
COPY index.html /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "test_app.py"]

