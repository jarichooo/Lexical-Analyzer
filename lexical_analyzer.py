"""
Core Lexical Analyzer Engine.
Supports Python, Java, and C++ source code analysis.
"""

from token import Token
import re


class LexicalAnalyzer:
    """
    Main lexical analyzer that supports multiple programming languages.
    """
    
    def __init__(self, language='python'):
        """
        Initialize the lexical analyzer for a specific language.
        
        Args:
            language (str): The programming language ('python', 'java', 'cpp')
        """
        self.language = language.lower()
        self.tokens = []
        self.errors = []
        self.line = 1
        self.column = 1
        self.current_pos = 0
        self.code = ""
        
        # Import language-specific lexer
        if self.language == 'python':
            from languages.python_lexer import PythonLexer
            self.lexer = PythonLexer()
        elif self.language == 'java':
            from languages.java_lexer import JavaLexer
            self.lexer = JavaLexer()
        elif self.language == 'cpp':
            from languages.cpp_lexer import CppLexer
            self.lexer = CppLexer()
        else:
            raise ValueError(f"Unsupported language: {language}")
    
    def tokenize(self, code):
        """
        Tokenize the given source code.
        
        Args:
            code (str): Source code to tokenize
            
        Returns:
            list: List of Token objects
        """
        self.code = code
        self.tokens = []
        self.errors = []
        self.line = 1
        self.column = 1
        self.current_pos = 0
        
        return self.lexer.tokenize(code)
    
    def tokenize_with_errors(self, code):
        """
        Tokenize code and return both tokens and errors.
        
        Args:
            code (str): Source code to tokenize
            
        Returns:
            tuple: (list of Token objects, list of error dictionaries)
        """
        tokens = self.tokenize(code)
        errors = self.lexer.get_errors()
        return tokens, errors


class BaseLexer:
    """
    Base class for language-specific lexers.
    """
    
    def __init__(self):
        self.tokens = []
        self.errors = []
        self.line = 1
        self.column = 1
        self.current_pos = 0
        self.code = ""
    
    def tokenize(self, code):
        """Tokenize source code. Must be implemented by subclasses."""
        raise NotImplementedError
    
    def add_token(self, token_type, value, line, column):
        """Add a token to the tokens list."""
        token = Token(token_type, value, line, column)
        self.tokens.append(token)
        return token
    
    def add_error(self, message, line, column):
        """Add an error to the errors list."""
        error = {
            'message': message,
            'line': line,
            'column': column
        }
        self.errors.append(error)
    
    def get_errors(self):
        """Get all accumulated errors."""
        return self.errors
    
    def peek(self, offset=0):
        """Peek at character without consuming it."""
        pos = self.current_pos + offset
        if pos < len(self.code):
            return self.code[pos]
        return None
    
    def consume(self):
        """Consume and return the current character."""
        if self.current_pos < len(self.code):
            char = self.code[self.current_pos]
            self.current_pos += 1
            if char == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            return char
        return None
    
    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.peek() and self.peek() in ' \t\n\r':
            self.consume()
    
    def is_digit(self, char):
        """Check if character is a digit."""
        return char and char.isdigit()
    
    def is_letter(self, char):
        """Check if character is a letter."""
        return char and char.isalpha()
    
    def is_identifier_start(self, char):
        """Check if character can start an identifier."""
        return self.is_letter(char) or char == '_'
    
    def is_identifier_char(self, char):
        """Check if character can be part of an identifier."""
        return self.is_letter(char) or self.is_digit(char) or char == '_'
