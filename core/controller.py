# core/controller.py

from PyQt5.QtCore import QObject, pyqtSignal

class MainController(QObject):
    """Contrôleur principal pour l'application"""
    execution_result = pyqtSignal(str, bool, str)
    log_message = pyqtSignal(str)
    module_loaded = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.modules = {}  # Tu peux y ajouter tes modules si besoin
        
    def execute_module(self, module_name):
        """Exécute un module spécifique"""
        try:
            # Implémente ici la logique d'exécution
            self.log_message.emit(f"Exécution du module {module_name}")
            # Simuler succès
            self.execution_result.emit(module_name, True, "Exécution réussie")
        except Exception as e:
            self.log_message.emit(f"Erreur lors de l'exécution de {module_name} : {str(e)}")
            self.execution_result.emit(module_name, False, str(e))
