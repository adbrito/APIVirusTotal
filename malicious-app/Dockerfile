# Usa la imagen oficial de Node.js como base
FROM node:14-alpine AS build

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el package.json y el package-lock.json (si existe) para instalar dependencias
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . .

# Compila la aplicación
RUN npm run build

# Usa una imagen ligera de Nginx para servir la aplicación compilada
FROM nginx:alpine

# Copia los archivos compilados de la aplicación React al directorio de contenido estático de Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Exponer el puerto 80 para que Nginx pueda servir la aplicación
EXPOSE 80

# Comando por defecto para iniciar Nginx y servir la aplicación React
CMD ["nginx", "-g", "daemon off;"]
