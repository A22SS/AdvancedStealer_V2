# controllers/module_controller.py
import importlib
import sys
import os
import subprocess
from PyQt5.QtCore import QObject, pyqtSignal

class ModuleController(QObject):
    execution_output = pyqtSignal(str)
    execution_error = pyqtSignal(str)
    execution_completed = pyqtSignal(bool, str)
    
    def __init__(self, module_path="./"):
        super().__init__()
        self.module_path = module_path
        self.current_process = None
    
    def execute_module(self, module_name, code_content=None):
        """Exécute un module spécifique par son nom"""
        try:
            # Si on a du code à exécuter directement
            if code_content:
                # Créer un fichier temporaire
                temp_file = f"temp_{module_name}.py"
                with open(temp_file, 'w') as f:
                    f.write(code_content)
                
                # Exécuter le fichier en tant que process séparé
                self.current_process = subprocess.Popen(
                    [sys.executable, temp_file],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                # Récupérer la sortie standard et les erreurs
                stdout, stderr = self.current_process.communicate()
                
                # Supprimer le fichier temporaire
                os.remove(temp_file)
                
                # Émettre les signaux
                if stdout:
                    self.execution_output.emit(stdout)
                if stderr:
                    self.execution_error.emit(stderr)
                
                success = self.current_process.returncode == 0
                message = f"Exécution {'réussie' if success else 'échouée'}"
                self.execution_completed.emit(success, message)
                
                return success
            
            # Sinon, on essaie d'importer et d'exécuter le module
            else:
                full_module_path = f"{self.module_path}.{module_name}"
                try:
                    # Importer le module dynamiquement
                    module = importlib.import_module(full_module_path)
                    # Recharger le module si nécessaire
                    module = importlib.reload(module)
                    
                    self.execution_output.emit(f"Module {module_name} importé avec succès.")
                    self.execution_completed.emit(True, "Importation réussie")
                    return True
                    
                except ImportError as e:
                    self.execution_error.emit(f"Erreur d'importation du module {module_name}: {str(e)}")
                    self.execution_completed.emit(False, f"Erreur d'importation: {str(e)}")
                    return False
                
        except Exception as e:
            self.execution_error.emit(f"Erreur lors de l'exécution du module {module_name}: {str(e)}")
            self.execution_completed.emit(False, f"Erreur d'exécution: {str(e)}")
            return False
    
    def stop_execution(self):
        """Arrête l'exécution du processus en cours"""
        if self.current_process and self.current_process.poll() is None:
            self.current_process.terminate()
            self.execution_output.emit("Exécution arrêtée par l'utilisateur.")
            return True
        return False
