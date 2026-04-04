import cv2
from http.server import BaseHTTPRequestHandler, HTTPServer
import serial
import rclpy
from std_msgs.msg import String

# 1. Inicializar ROS 2
rclpy.init()
node = rclpy.create_node('cerebro_faraon')
publisher = node.create_publisher(String, '/comando_luz', 10)

# 2. Conectar al Hardware (Arduino)
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    print("✅ Arduino Conectado")
except:
    print("❌ Error: No veo el Arduino")
    ser = None

# 3. Conectar a la Cámara
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

class FaraonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <html>
            <body style="text-align:center; background:#1a1a1a; color:white; font-family:sans-serif; padding-top:20px;">
                <h1 style="color:#f1c40f;">👑 FARAÓN TOTAL 2026 👑</h1>
                <div style="border:5px solid #f1c40f; display:inline-block; border-radius:10px; overflow:hidden; background:black;">
                    <img src="/video" width="100%">
                </div>
                <br><br>
                <a href="/on"><button style="padding:40px; background:green; color:white; width:90%; font-size:25px; border-radius:15px; border:none;">ENCENDER LUZ</button></a>
                <br><br>
                <a href="/off"><button style="padding:40px; background:red; color:white; width:90%; font-size:25px; border-radius:15px; border:none;">APAGAR LUZ</button></a>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        
        elif self.path == '/video':
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            while True:
                success, frame = camera.read()
                if not success: break
                _, jpeg = cv2.imencode('.jpg', frame)
                self.wfile.write(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

        elif self.path in ['/on', '/off']:
            valor = "1" if self.path == '/on' else "0"
            if ser: ser.write(valor.encode()) # Mando directo al cable
            print(f"🔦 Orden enviada: {valor}")
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

print("🚀 Faraón Total Online en Puerto 8000...")
HTTPServer(('0.0.0.0', 8000), FaraonHandler).serve_forever()
