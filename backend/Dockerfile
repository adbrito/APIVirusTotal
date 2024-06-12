# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos (si tienes uno) e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el archivo .env al contenedor
COPY .env .env

# Carga las variables de entorno desde el archivo .env
ENV $(cat .env | xargs)

# Copia el resto de tu aplicación en el contenedor
COPY . .

# Comando por defecto para ejecutar tu aplicación Flask
CMD ["python", "app.py"]
