#!/usr/bin/python3
"""
Task 3: Develop a simple API using Python with http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


HOST = "0.0.0.0"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Simple API Handler"""

    def _send_json(self, data, status_code=200):
        """Send a JSON response"""
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _send_text(self, text, status_code=200):
        """Send a plain text response"""
        payload = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self._send_text("Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text("OK")
        elif self.path == "/data":
            self._send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self._send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })
        else:
            self._send_text("Endpoint not found", 404)


def run_server():
    """Start the HTTP server"""
    server = HTTPServer((HOST, PORT), SimpleAPIHandler)
    print(f"Server running on http://localhost:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()

