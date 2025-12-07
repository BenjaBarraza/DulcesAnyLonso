# Usamos una imagen ligera de Python oficial
FROM python:3.10-slim

# Evita que Python genere archivos .pyc y fuerza la salida por consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Creamos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los requerimientos e instalamos las dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiamos el resto del código del proyecto
COPY . /app/

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para iniciar el servidor (escuchando en todas las interfaces)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]