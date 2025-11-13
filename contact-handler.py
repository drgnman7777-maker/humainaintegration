#!/usr/bin/env python3
"""
Simple contact form handler for HumAIna Integration
Sends emails using local mail system
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess

class ContactHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        if self.path == '/contact':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                
                # Log to file (simple solution)
                with open('/home/havenai/contact-submissions.log', 'a') as f:
                    f.write(f"\n{'='*50}\n")
                    f.write(f"Date: {subprocess.check_output(['date']).decode().strip()}\n")
                    f.write(f"Name: {data['name']}\n")
                    f.write(f"Email: {data['email']}\n")
                    f.write(f"Message: {data['message']}\n")
                
                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {'status': 'success', 'message': 'Contact form submitted successfully'}
                self.wfile.write(json.dumps(response).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {'status': 'error', 'message': str(e)}
                self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8001), ContactHandler)
    print('Contact form handler running on port 8001...')
    server.serve_forever()