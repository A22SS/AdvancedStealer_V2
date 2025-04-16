# ui/module_tabs.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QLabel
from gui.code_editor import CodeEditor

class ModuleTab(QWidget):
    """Onglet de base pour un module"""
    
    def __init__(self, name, file_path=None, parent=None):
        super().__init__(parent)
        self.name = name
        self.file_path = file_path
        
        # Layout principal
        self.layout = QVBoxLayout(self)
        
        # Titre du module
        if name:
            title = QLabel(f"Module: {name}")
            title.setStyleSheet("font-weight: bold; font-size: 14px; color: #3daee9;")
            self.layout.addWidget(title)
        
        # Éditeur de code
        self.code_editor = CodeEditor()
        self.layout.addWidget(self.code_editor)
        
        # Boutons d'action
        actions_layout = QHBoxLayout()
        
        self.run_button = QPushButton("Exécuter")
        self.run_button.setStyleSheet("background-color: #27ae60; color: white;")
        actions_layout.addWidget(self.run_button)
        
        self.save_button = QPushButton("Sauvegarder")
        actions_layout.addWidget(self.save_button)
        
        self.layout.addLayout(actions_layout)
        
        # Charger le contenu du fichier si disponible
        if file_path:
            self.load_file(file_path)
    
    def load_file(self, file_path):
        """Charge le contenu d'un fichier dans l'éditeur"""
        try:
            with open(file_path, 'r') as f:
                self.code_editor.setPlainText(f.read())
        except Exception as e:
            print(f"Erreur lors du chargement du fichier {file_path}: {str(e)}")
    
    def get_code(self):
        """Récupère le code actuel de l'éditeur"""
        return self.code_editor.toPlainText()
    
    def set_code(self, code):
        """Définit le code dans l'éditeur"""
        self.code_editor.setPlainText(code)

class ModuleTabs(QTabWidget):
    """Gestionnaire d'onglets pour les modules"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Configuration des onglets
        self.setTabPosition(QTabWidget.North)
        self.setMovable(True)
        self.setDocumentMode(True)
        
        # Dictionnaire des modules
        self.module_tabs = {}
    
    def add_module(self, name, file_path=None):
        """Ajoute un nouvel onglet de module"""
        module_tab = ModuleTab(name, file_path)
        self.addTab(module_tab, name)
        self.module_tabs[name] = module_tab
        return module_tab
    
    def get_module(self, name):
        """Récupère un onglet de module par son nom"""
        return self.module_tabs.get(name)
    
    def get_current_module(self):
        """Récupère l'onglet de module actuellement sélectionné"""
        current_widget = self.currentWidget()
        if isinstance(current_widget, ModuleTab):
            return current_widget
        return None
