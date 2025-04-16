import subprocess
import psutil
import winreg
import ctypes
import os
import socket
import platform

class SystemOperations:
    @staticmethod
    def get_username():
        return os.getlogin()

    @staticmethod
    def get_computer_name():
        return socket.gethostname()

    @staticmethod
    def get_operating_system():
        return platform.system() + " " + platform.release()

    @staticmethod
    def check_privileges():
        privileges = ctypes.windll.shell32.IsUserAnAdmin()
        return privileges == 1

    @staticmethod
    def run_command(command):
        result = subprocess.run(command, shell=True, capture_output=True)
        return result.stdout.decode() if result.stdout else result.stderr.decode()

    @staticmethod
    def get_running_processes():
        return [proc.info for proc in psutil.process_iter(['pid', 'name'])]

    @staticmethod
    def get_environment_variables():
        return os.environ

    @staticmethod
    def alter_registry(key_path, value):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValue(key, value, winreg.REG_SZ, "1")
            winreg.CloseKey(key)
            return True
        except WindowsError as e:
            print(f"Erreur lors de la modification du registre : {e}")
            return False

system_ops = SystemOperations()
