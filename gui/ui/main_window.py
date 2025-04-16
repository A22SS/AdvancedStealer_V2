
from core.payloads import PayloadFactory  
from gui.controllers.module_controller import ModuleController

import sys
import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTreeView, QSplitter, QTextEdit, QLabel, QStatusBar, QToolBar, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import qdarkstyle

class AdvancedStealerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.setWindowTitle("AdvancedStealer GUI v2.0")
        self.setGeometry(100, 100, 1200, 800)
        
        # Définition du thème sombre par défaut
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        
        # Création du widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Layout principal
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Création de la barre d'outils
        self.create_toolbar()
        
        # Création du splitter horizontal principal
        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_layout.addWidget(self.main_splitter)
        
        # Création de l'arborescence des modules (gauche)
        self.module_tree = self.create_module_tree()
        self.main_splitter.addWidget(self.module_tree)
        
        # Zone principale de contenu (droite)
        self.content_widget = QTabWidget()
        self.main_splitter.addWidget(self.content_widget)
        
        # Ajout des onglets pour chaque module
        self.add_module_tabs()
        
        # Barre de statut
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Prêt")
        
        # Définition des proportions du splitter
        self.main_splitter.setSizes([300, 900])
        
        # Connexion des signaux
        self.connect_signals()
    
    def create_toolbar(self):
        # Création de la barre d'outils
        toolbar = QToolBar("Barre d'outils principale")
        self.addToolBar(toolbar)
        
        # Action Exécuter
        import os
        icon_path = os.path.join(os.path.dirname(__file__),"../../resources/icons/run.png")
        self.action_run = QAction(QIcon(icon_path), "Exécuter", self)
        self.action_run.setShortcut("F5")
        toolbar.addAction(self.action_run)
        
        # Action Arrêter
        import os
        icon_path_stop = os.path.join(os.path.dirname(__file__), "../../resources/icons/run.png")
        self.action_stop = QAction(QIcon(icon_path_stop), "Arrêter", self)
        self.action_stop.setShortcut("F6")
        toolbar.addAction(self.action_stop)
        
        toolbar.addSeparator()
        
        # Action Thème clair/sombre
        import os
        icon_path_theme = os.path.join(os.path.dirname(__file__), "../../resources/icons/theme.png")
        self.action_theme = QAction(QIcon(icon_path_theme), "Changer de thème", self)
        toolbar.addAction(self.action_theme)
        
        # Action Ouvrir
        import os
        icon_path_open = os.path.join(os.path.dirname(__file__), "../../resources/icons/open.png")
        self.action_open = QAction(QIcon(icon_path_open), "Ouvrir un fichier", self)
        toolbar.addAction(self.action_open)
        
        # Action Sauvegarder
        import os
        icon_path_save = os.path.join(os.path.dirname(__file__), "../../resources/icons/save.png")
        self.action_save = QAction(QIcon(icon_path_save), "Sauvegarder", self)
        toolbar.addAction(self.action_save)
    
    def create_module_tree(self):
        # Création d'un widget pour contenir l'arborescence
        tree_widget = QWidget()
        tree_layout = QVBoxLayout(tree_widget)
        
        # Titre de l'arborescence
        tree_title = QLabel("Modules AdvancedStealer")
        tree_title.setStyleSheet("font-weight: bold; color: #3daee9;")
        tree_layout.addWidget(tree_title)
        
        # Arborescence des modules
        tree_view = QTreeView()
        tree_view.setHeaderHidden(True)
        # Ici, nous devrons implémenter un modèle personnalisé pour l'arborescence
        tree_layout.addWidget(tree_view)
        
        return tree_widget
    
    def add_module_tabs(self):
        # Ajout des onglets pour chaque module principal
        modules = [
            ("Core", self.create_core_tab()),
            ("Evasion", self.create_evasion_tab()),
            ("Exploit", self.create_exploit_tab()),
            ("Crypto Harvesting", self.create_crypto_tab()),
            ("Exfil", self.create_exfil_tab()),
            ("Persistence", self.create_persistence_tab()),
            ("Utilities", self.create_utilities_tab()),
            ("Logs", self.create_logs_tab())
        ]
        
        for name, widget in modules:
            self.content_widget.addTab(widget, name)
    
    def create_core_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sous-onglets pour les composants du module Core
        sub_tabs = QTabWidget()
        
        # Onglet PayloadFactory
        payload_tab = QWidget()
        payload_layout = QVBoxLayout(payload_tab)
        
        # Éditeur de code pour PayloadFactory
        payload_editor = QTextEdit()
        payload_editor.setPlaceholderText("# Code de payloads.py ici")
        payload_layout.addWidget(payload_editor)
        
        # Boutons d'action
        payload_actions = QHBoxLayout()
        btn_run_payload = QPushButton("Exécuter")
        btn_run_payload.setStyleSheet("background-color: #27ae60; color: white;")
        payload_actions.addWidget(btn_run_payload)
        
        btn_save_payload = QPushButton("Sauvegarder")
        payload_actions.addWidget(btn_save_payload)
        payload_layout.addLayout(payload_actions)
        
        sub_tabs.addTab(payload_tab, "PayloadFactory")
        
        # Onglet MutationEngine
        mutation_tab = QWidget()
        mutation_layout = QVBoxLayout(mutation_tab)
        
        # Éditeur de code pour MutationEngine
        mutation_editor = QTextEdit()
        mutation_editor.setPlaceholderText("# Code de polymorphic_engine.py ici")
        mutation_layout.addWidget(mutation_editor)
        
        # Boutons d'action
        mutation_actions = QHBoxLayout()
        btn_run_mutation = QPushButton("Exécuter")
        btn_run_mutation.setStyleSheet("background-color: #27ae60; color: white;")
        mutation_actions.addWidget(btn_run_mutation)
        
        btn_save_mutation = QPushButton("Sauvegarder")
        mutation_actions.addWidget(btn_save_mutation)
        mutation_layout.addLayout(mutation_actions)
        
        sub_tabs.addTab(mutation_tab, "MutationEngine")
        
        layout.addWidget(sub_tabs)
        return tab
    
    # Méthodes similaires pour les autres onglets de modules
    def create_evasion_tab(self):
        # Structure similaire à create_core_tab
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Éditeur de code pour EvasionTools
        evasion_editor = QTextEdit()
        evasion_editor.setPlaceholderText("# Code de evade_detection.py ici")
        layout.addWidget(evasion_editor)
        
        # Boutons d'action
        actions = QHBoxLayout()
        btn_run = QPushButton("Exécuter")
        btn_run.setStyleSheet("background-color: #27ae60; color: white;")
        actions.addWidget(btn_run)
        
        btn_save = QPushButton("Sauvegarder")
        actions.addWidget(btn_save)
        layout.addLayout(actions)
        
        return tab
    
    def create_exploit_tab(self):
        # Structure pour le module Exploit
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sous-onglets
        sub_tabs = QTabWidget()
        
        # Onglet PDF Embedder
        pdf_tab = QWidget()
        pdf_layout = QVBoxLayout(pdf_tab)
        pdf_editor = QTextEdit()
        pdf_editor.setPlaceholderText("# Code de pdf_embedder.py ici")
        pdf_layout.addWidget(pdf_editor)
        
        # Boutons d'action
        pdf_actions = QHBoxLayout()
        btn_run_pdf = QPushButton("Exécuter")
        btn_run_pdf.setStyleSheet("background-color: #27ae60; color: white;")
        pdf_actions.addWidget(btn_run_pdf)
        btn_save_pdf = QPushButton("Sauvegarder")
        pdf_actions.addWidget(btn_save_pdf)
        pdf_layout.addLayout(pdf_actions)
        
        sub_tabs.addTab(pdf_tab, "PDF Embedder")
        
        # Onglet Dropper Creator
        dropper_tab = QWidget()
        dropper_layout = QVBoxLayout(dropper_tab)
        dropper_editor = QTextEdit()
        dropper_editor.setPlaceholderText("# Code de dropper_creator.py ici")
        dropper_layout.addWidget(dropper_editor)
        
        # Boutons d'action
        dropper_actions = QHBoxLayout()
        btn_run_dropper = QPushButton("Exécuter")
        btn_run_dropper.setStyleSheet("background-color: #27ae60; color: white;")
        dropper_actions.addWidget(btn_run_dropper)
        btn_save_dropper = QPushButton("Sauvegarder")
        dropper_actions.addWidget(btn_save_dropper)
        dropper_layout.addLayout(dropper_actions)
        
        sub_tabs.addTab(dropper_tab, "Dropper Creator")
        
        layout.addWidget(sub_tabs)
        return tab
    
    def create_crypto_tab(self):
        # Méthode similaire pour le module Crypto Harvesting
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sous-onglets
        sub_tabs = QTabWidget()
        
        # Onglets pour chaque composant
        components = [
            ("WalletHunter", "# Code de wallet_hunter.py ici"),
            ("WalletDecryptor", "# Code de wallet_decryptor.py ici"),
            ("APIScraper", "# Code de api_scrapers.py ici")
        ]
        
        for name, placeholder in components:
            component_tab = QWidget()
            component_layout = QVBoxLayout(component_tab)
            
            editor = QTextEdit()
            editor.setPlaceholderText(placeholder)
            component_layout.addWidget(editor)
            
            actions = QHBoxLayout()
            btn_run = QPushButton("Exécuter")
            btn_run.setStyleSheet("background-color: #27ae60; color: white;")
            actions.addWidget(btn_run)
            
            btn_save = QPushButton("Sauvegarder")
            actions.addWidget(btn_save)
            component_layout.addLayout(actions)
            
            sub_tabs.addTab(component_tab, name)
        
        layout.addWidget(sub_tabs)
        return tab
    
    def create_exfil_tab(self):
        # Méthode similaire pour le module Exfil
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sous-onglets
        sub_tabs = QTabWidget()
        
        # Onglets pour chaque composant
        components = [
            ("DataAggregator", "# Code de aggregator.py ici"),
            ("Exfiltrator", "# Code de exfiltration_methods.py ici")
        ]
        
        for name, placeholder in components:
            component_tab = QWidget()
            component_layout = QVBoxLayout(component_tab)
            
            editor = QTextEdit()
            editor.setPlaceholderText(placeholder)
            component_layout.addWidget(editor)
            
            actions = QHBoxLayout()
            btn_run = QPushButton("Exécuter")
            btn_run.setStyleSheet("background-color: #27ae60; color: white;")
            actions.addWidget(btn_run)
            
            btn_save = QPushButton("Sauvegarder")
            actions.addWidget(btn_save)
            component_layout.addLayout(actions)
            
            sub_tabs.addTab(component_tab, name)
        
        layout.addWidget(sub_tabs)
        return tab
    
    def create_persistence_tab(self):
        # Méthode similaire pour le module Persistence
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sous-onglets
        sub_tabs = QTabWidget()
        
        # Onglets pour chaque composant
        components = [
            ("PersistenceMethods", "# Code de persistence_methods.py ici"),
            ("AutoRun", "# Code de autorun.py ici")
        ]
        
        for name, placeholder in components:
            component_tab = QWidget()
            component_layout = QVBoxLayout(component_tab)
            
            editor = QTextEdit()
            editor.setPlaceholderText(placeholder)
            component_layout.addWidget(editor)
            
            actions = QHBoxLayout()
            btn_run = QPushButton("Exécuter")
            btn_run.setStyleSheet("background-color: #27ae60; color: white;")
            actions.addWidget(btn_run)
            
            btn_save = QPushButton("Sauvegarder")
            actions.addWidget(btn_save)
            component_layout.addLayout(actions)
            
            sub_tabs.addTab(component_tab, name)
        
        layout.addWidget(sub_tabs)
        return tab
    
    def create_utilities_tab(self):
        # Méthode similaire pour le module Utilities
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sous-onglets
        sub_tabs = QTabWidget()
        
        # Onglets pour chaque composant
        components = [
            ("FileOperations", "# Code de file_operations.py ici"),
            ("NetworkOperations", "# Code de network_operations.py ici"),
            ("SystemOperations", "# Code de system_operations.py ici")
        ]
        
        for name, placeholder in components:
            component_tab = QWidget()
            component_layout = QVBoxLayout(component_tab)
            
            editor = QTextEdit()
            editor.setPlaceholderText(placeholder)
            component_layout.addWidget(editor)
            
            actions = QHBoxLayout()
            btn_run = QPushButton("Exécuter")
            btn_run.setStyleSheet("background-color: #27ae60; color: white;")
            actions.addWidget(btn_run)
            
            btn_save = QPushButton("Sauvegarder")
            actions.addWidget(btn_save)
            component_layout.addLayout(actions)
            
            sub_tabs.addTab(component_tab, name)
        
        layout.addWidget(sub_tabs)
        return tab
    
    def create_logs_tab(self):
        # Onglet pour les logs
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Zone de logs
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet("background-color: #2d2d2d; color: #d3d7cf;")
        layout.addWidget(self.log_output)
        
        # Boutons pour les logs
        log_actions = QHBoxLayout()
        btn_clear_logs = QPushButton("Effacer les logs")
        log_actions.addWidget(btn_clear_logs)
        
        btn_save_logs = QPushButton("Sauvegarder les logs")
        log_actions.addWidget(btn_save_logs)
        
        layout.addLayout(log_actions)
        
        return tab
    
    def connect_signals(self):
        # Connexion des signaux aux slots
        self.action_theme.triggered.connect(self.toggle_theme)
        self.action_run.triggered.connect(self.run_current_module)
        self.action_stop.triggered.connect(self.stop_execution)
        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save_file)
    
    def toggle_theme(self):
        # Alternance entre thème clair et sombre
        if "qdarkstyle" in self.styleSheet():
            self.setStyleSheet("")
        else:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    def run_current_module(self):
        # Exécution du module actuellement sélectionné
        current_tab = self.content_widget.currentWidget()
        current_tab_name = self.content_widget.tabText(self.content_widget.currentIndex())
        self.log_output.append(f"[INFO] Exécution du module {current_tab_name}...")
        self.statusBar.showMessage(f"Exécution de {current_tab_name}...")
        
        # Ici, vous implémenteriez la logique pour exécuter le module sélectionné
        # Pour l'exemple, nous allons simplement simuler une exécution
        self.log_output.append(f"[SUCCESS] Module {current_tab_name} exécuté avec succès.")
        self.statusBar.showMessage("Prêt")
    
    def stop_execution(self):
        # Arrêt de l'exécution en cours
        self.log_output.append("[INFO] Arrêt de l'exécution en cours...")
        self.statusBar.showMessage("Exécution arrêtée")
    
    def open_file(self):
        # Ouverture d'un fichier
        file_path, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Fichiers Python (*.py);;Tous les fichiers (*)")
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Détermine quel éditeur doit recevoir le contenu en fonction du nom de fichier
                file_name = os.path.basename(file_path)
                self.log_output.append(f"[INFO] Fichier ouvert: {file_path}")
                
                # Ici, vous implémenteriez la logique pour déterminer quel éditeur doit recevoir le contenu
                
            except Exception as e:
                self.log_output.append(f"[ERROR] Erreur lors de l'ouverture du fichier: {str(e)}")
    
    def save_file(self):
        # Sauvegarde du fichier actuel
        file_path, _ = QFileDialog.getSaveFileName(self, "Sauvegarder le fichier", "", "Fichiers Python (*.py);;Tous les fichiers (*)")
        if file_path:
            try:
                # Ici, vous implémenteriez la logique pour récupérer le contenu de l'éditeur actuel
                content = "# Contenu à sauvegarder"
                
                with open(file_path, 'w') as f:
                    f.write(content)
                
                self.log_output.append(f"[INFO] Fichier sauvegardé: {file_path}")
                
            except Exception as e:
                self.log_output.append(f"[ERROR] Erreur lors de la sauvegarde du fichier: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedStealerGUI()
    window.show()
    sys.exit(app.exec_())
