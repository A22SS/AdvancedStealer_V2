#!/usr/bin/env python3
# main.py - Point d'entrée principal (version corrigée)

import sys
import os
import logging
from PyQt5.QtWidgets import QApplication
from gui.ui.main_window import AdvancedStealerGUI

# Configuration du système de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("advanced_stealer.log"),
        logging.StreamHandler()
    ]
)

def main():
    """Point d'entrée principal"""
    app = QApplication(sys.argv)
    
    try:
        # Résolution des chemins pour les imports
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
        
        # Initialisation de l'interface
        window = AdvancedStealerGUI()
        window.show()
        
        return app.exec_()
        
    except Exception as e:
        logging.critical(f"ERREUR FATALE : {str(e)}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
