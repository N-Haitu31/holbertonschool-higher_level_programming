#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code=200, content_type="text/plain", body=""):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        if isinstance(body, str):
            self.wfile.write(body.encode("utf-8"))
        else:
            self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send_response(200, "text/plain", "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self._send_response(200, "application/json", json_data)

        elif self.path == "/status":
            self._send_response(200, "text/plain", "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            json_info = json.dumps(info)
            self._send_response(200, "application/json", json_info)

        else:
            self._send_response(404, "text/plain", "Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting server on http://localhost:{}".format(port))
    httpd.serve_forever()


if __name__ == "__main__":
    run()
