from PyQt5.QtCore import QObject, pyqtSignal
import yaml
import logging

class MainController(QObject):
    """Contrôleur principal pour la logique métier de l'application"""
    
    execution_result = pyqtSignal(str, bool, str)
    log_message = pyqtSignal(str)
    module_loaded = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.modules = {
            'payload': None,  # Sera initialisé lors du chargement
            'mutation': None,
            'evasion': None,
            'crypto': None,
            'exfil': None,
            'persistence': None,
            'exploit': None,
        }
        self.current_config = {}
        self.initialize_modules()
        
    def initialize_modules(self):
        """Initialise les modules requis"""
        try:
            from core.payloads import PayloadFactory
            from core.polymorphic_engine import MutationEngine
            from evasion.evade_detection import EvasionTools
            
            self.modules['payload'] = PayloadFactory()
            self.modules['mutation'] = MutationEngine()
            self.modules['evasion'] = EvasionTools()
            
            self.log_message.emit("Modules principaux initialisés")
        except Exception as e:
            self.log_message.emit(f"Erreur d'initialisation: {str(e)}")
    
    def execute_module(self, module_name, parameters=None):
        """Exécute un module spécifique avec paramètres optionnels"""
        try:
            module = self.modules.get(module_name)
            if not module:
                raise ValueError(f"Module {module_name} non initialisé ou introuvable")
                
            result = module.run(parameters) if parameters else module.run()
            self.execution_result.emit(module_name, True, str(result))
            self.log_message.emit(f"Module {module_name} exécuté avec succès")
            return result
            
        except Exception as e:
            self.execution_result.emit(module_name, False, str(e))
            self.log_message.emit(f"Erreur dans l'exécution de {module_name}: {str(e)}")
            logging.error(f"Exception dans {module_name}: {str(e)}", exc_info=True)
            return None
    
    def save_configuration(self, config_path):
        """Sauvegarde la configuration dans un fichier YAML"""
        try:
            with open(config_path, 'w') as f:
                yaml.safe_dump(self.current_config, f)
            self.log_message.emit(f"Configuration sauvegardée: {config_path}")
            return True
        except Exception as e:
            self.log_message.emit(f"Erreur lors de la sauvegarde: {str(e)}")
            return False
    
    def load_configuration(self, config_path):
        """Charge une configuration depuis un fichier YAML"""
        try:
            with open(config_path, 'r') as f:
                self.current_config = yaml.safe_load(f)
            self.log_message.emit(f"Configuration chargée: {config_path}")
            return self.current_config
        except Exception as e:
            self.log_message.emit(f"Erreur lors du chargement: {str(e)}")
            return None

    def get_modules(self):
        """Retourne la liste des modules disponibles"""
        return list(self.modules.keys())
