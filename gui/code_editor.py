# controllers/code_editor.py
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFont, QColor, QTextCharFormat, QSyntaxHighlighter
from PyQt5.QtCore import QRegExp

class PythonHighlighter(QSyntaxHighlighter):
    """Surligneur de syntaxe Python pour QTextEdit"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Formats de mise en forme
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Bold)
        
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))
        
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))
        
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))
        
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))
        
        # Mots-clés Python
        keywords = [
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
            'del', 'elif', 'else', 'except', 'exec', 'finally', 'for',
            'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not',
            'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with',
            'yield', 'self', 'None', 'True', 'False'
        ]
        
        # Règles de coloration
        self.highlighting_rules = []
        
        # Règle pour les mots-clés
        for keyword in keywords:
            pattern = QRegExp(r'\b' + keyword + r'\b')
            self.highlighting_rules.append((pattern, keyword_format))
        
        # Règle pour les fonctions
        pattern = QRegExp(r'\b[A-Za-z0-9_]+(?=\()')
        self.highlighting_rules.append((pattern, function_format))
        
        # Règle pour les chaînes de caractères
        pattern = QRegExp(r'"[^"]*"')
        self.highlighting_rules.append((pattern, string_format))
        pattern = QRegExp(r"'[^']*'")
        self.highlighting_rules.append((pattern, string_format))
        
        # Règle pour les commentaires
        pattern = QRegExp(r'#[^\n]*')
        self.highlighting_rules.append((pattern, comment_format))
        
        # Règle pour les nombres
        pattern = QRegExp(r'\b[0-9]+\b')
        self.highlighting_rules.append((pattern, number_format))
    
    def highlightBlock(self, text):
        """Applique la coloration syntaxique au bloc de texte"""
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

class CodeEditor(QTextEdit):
    """Éditeur de code avec coloration syntaxique"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Configuration de la police
        font = QFont('Consolas', 10)
        font.setFixedPitch(True)
        self.setFont(font)
        
        # Configuration des tabulations
        self.setTabStopWidth(4 * self.fontMetrics().width(' '))
        
        # Ajout du surligneur de syntaxe
        self.highlighter = PythonHighlighter(self.document())
