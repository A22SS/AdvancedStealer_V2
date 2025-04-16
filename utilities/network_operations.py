import requests
import socket
import dns.resolver
import smtplib

class NetworkOperations:
    @staticmethod
    def get_external_ip():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(('8.8.8.8', 1))
                return s.getsockname()[0]
        except socket.error:
            return None

    @staticmethod
    def resolve_hostname(hostname):
        try:
            return str(dns.resolver.resolve(hostname, 'A')[0])
        except dns.resolver.NXDOMAIN:
            return None

    @staticmethod
    def send_post(server_url, data):
        try:
            response = requests.post(server_url, data=data)
            return response.status_code == 200
        except requests.RequestException:
            return False

    @staticmethod
    def dns_query(domain, record_type='A'):
        try:
            return str(dns.resolver.resolve(domain, record_type)[0])
        except dns.resolver.NXDOMAIN:
            return None

    @staticmethod
    def email_setup(smtp_server, smtp_port, username, password, sender_email):
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(username, password)
            return server, sender_email
        except Exception as e:
            print(f"Echec de la configuration SMTP : {e}")
            return None, None

network_ops = NetworkOperations()
