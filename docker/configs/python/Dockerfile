# Usar la imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos.
COPY requirements.txt /app
COPY app.py /app
COPY index.html /app/index.html

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]

