# Usa una imagen base de Python
FROM python:3.9-slim
# Establece el directorio de trabajo
WORKDIR /app
# Copia la aplicación y la ejecuta
COPY app.py .
CMD ["python", "app.py"]