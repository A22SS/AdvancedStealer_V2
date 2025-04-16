# main.py (version corrigée)
import sys  # Import manquant ajouté ici
import os
import logging
from PyQt5.QtWidgets import QApplication
from gui.ui.main_window import AdvancedStealerGUI

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("advanced_stealer.log"),
        logging.StreamHandler()
    ]
)

def main():
    app = QApplication(sys.argv)
    
    # Résolution des chemins pour les imports
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    try:
        window = AdvancedStealerGUI()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logging.critical(f"ERREUR : {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
