# app.py

import os
import http.server
import socketserver

# El puerto que usará Cloud Run para exponer la aplicación
PORT = int(os.environ.get("PORT", 8080))

# Define un manejador simple que siempre responde con el mismo texto
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 1. Código de respuesta HTTP
        self.send_response(200)
        # 2. Encabezado de la respuesta (le dice al navegador que es texto plano)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # 3. Contenido de la respuesta
        response_text = "¡Despliegue CI/CD exitoso con solo Python estándar! 🎉"
        self.wfile.write(response_text.encode('utf-8'))

# Inicia el servidor
print(f"Sirviendo en el puerto {PORT}")
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    httpd.serve_forever()