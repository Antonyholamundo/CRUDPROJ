# Usa una imagen base de Pyth
FROM python:3.9-slim
# Establece el directorio de 
WORKDIR /app
# Copia la aplicación y la ejec
COPY app.py .

CMD ["python", "app.py"]


