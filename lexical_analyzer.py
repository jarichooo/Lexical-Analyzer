"""
Lexical Analyzer for Python, Java, and C++
Tokenizes source code and outputs tokens with their types as a dictionary
"""

import re
from enum import Enum
from typing import List, Dict, Tuple

class TokenType(Enum):
    """Token types for lexical analysis"""
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    STRING = "STRING"
    CHARACTER = "CHARACTER"
    OPERATOR = "OPERATOR"
    PUNCTUATION = "PUNCTUATION"
    COMMENT = "COMMENT"
    PREPROCESSOR = "PREPROCESSOR"
    ERROR = "ERROR"
    EOF = "EOF"


class Token:
    """Represents a single token"""
    def __init__(self, type_: TokenType, value: str, line: int, column: int):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def to_dict(self) -> Dict:
        """Convert token to dictionary representation"""
        return {
            "type": self.type.value,
            "value": self.value,
            "line": self.line,
            "column": self.column
        }
    
    def __repr__(self) -> str:
        return f"Token({self.type.value}, '{self.value}', {self.line}, {self.column})"


class LexicalAnalyzer:
    """Main lexical analyzer supporting Python, Java, and C++"""
    
    # Python keywords
    PYTHON_KEYWORDS = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
        'while', 'with', 'yield'
    }
    
    # Java keywords
    JAVA_KEYWORDS = {
        'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch',
        'char', 'class', 'const', 'continue', 'default', 'do', 'double',
        'else', 'enum', 'extends', 'final', 'finally', 'float', 'for',
        'goto', 'if', 'implements', 'import', 'instanceof', 'int', 'interface',
        'long', 'native', 'new', 'package', 'private', 'protected', 'public',
        'return', 'short', 'static', 'strictfp', 'super', 'switch',
        'synchronized', 'this', 'throw', 'throws', 'transient', 'try',
        'void', 'volatile', 'while'
    }
    
    # C++ keywords
    CPP_KEYWORDS = {
        'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel',
        'atomic_commit', 'atomic_noexcept', 'auto', 'bitand', 'bitor',
        'bool', 'break', 'case', 'catch', 'char', 'char8_t', 'char16_t',
        'char32_t', 'class', 'compl', 'concept', 'const', 'consteval',
        'constexpr', 'constinit', 'const_cast', 'continue', 'co_await',
        'co_return', 'co_yield', 'decltype', 'default', 'delete', 'do',
        'double', 'dynamic_cast', 'else', 'enum', 'explicit', 'export',
        'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline',
        'int', 'long', 'mutable', 'namespace', 'new', 'noexcept', 'not',
        'not_eq', 'nullptr', 'operator', 'or', 'or_eq', 'private', 'protected',
        'public', 'register', 'reinterpret_cast', 'requires', 'return', 'short',
        'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct',
        'switch', 'synchronized', 'template', 'this', 'thread_local', 'throw',
        'true', 'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned',
        'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while', 'xor',
        'xor_eq'
    }
    
    # Operators for all languages
    OPERATORS = {
        '+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
        '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '+=', '-=', '*=',
        '/=', '%=', '&=', '|=', '^=', '<<=', '>>=', '++', '--', '->', '::', 
        '?', ':', '.', '..'
    }
    
    # Punctuation for all languages
    PUNCTUATION = {
        '(', ')', '{', '}', '[', ']', ';', ',', '.', '@', '#', '$'
    }
    
    def __init__(self, language: str):
        """
        Initialize lexical analyzer for specified language
        
        Args:
            language: 'python', 'java', or 'cpp'
        """
        self.language = language.lower()
        if self.language not in ['python', 'java', 'cpp']:
            raise ValueError(f"Unsupported language: {language}")
        
        self.keywords = self._get_keywords()
        self.position = 0
        self.line = 1
        self.column = 1
        self.code = ""
        self.tokens: List[Token] = []
    
    def _get_keywords(self) -> set:
        """Get keywords for the specified language"""
        if self.language == 'python':
            return self.PYTHON_KEYWORDS
        elif self.language == 'java':
            return self.JAVA_KEYWORDS
        else:  # cpp
            return self.CPP_KEYWORDS
    
    def _current_char(self) -> str:
        """Get current character"""
        if self.position >= len(self.code):
            return '\0'
        return self.code[self.position]
    
    def _peek_char(self, offset: int = 1) -> str:
        """Peek ahead at character"""
        pos = self.position + offset
        if pos >= len(self.code):
            return '\0'
        return self.code[pos]
    
    def _advance(self) -> str:
        """Move to next character and return current"""
        char = self._current_char()
        self.position += 1
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char
    
    def _skip_whitespace(self):
        """Skip whitespace characters"""
        while self._current_char() in ' \t\n\r':
            self._advance()
    
    def _read_number(self) -> Token:
        """Read numeric literal"""
        start_line = self.line
        start_column = self.column
        num_str = ''
        
        # Handle hex, binary, octal
        if self.language == 'cpp' and self._current_char() == '0':
            if self._peek_char() == 'x' or self._peek_char() == 'X':
                num_str += self._advance()  # 0
                num_str += self._advance()  # x
                while self._current_char() in '0123456789abcdefABCDEF':
                    num_str += self._advance()
                return Token(TokenType.NUMBER, num_str, start_line, start_column)
            elif self._peek_char() == 'b' or self._peek_char() == 'B':
                num_str += self._advance()  # 0
                num_str += self._advance()  # b
                while self._current_char() in '01':
                    num_str += self._advance()
                return Token(TokenType.NUMBER, num_str, start_line, start_column)
        
        # Regular number
        while self._current_char().isdigit():
            num_str += self._advance()
        
        # Decimal point
        if self._current_char() == '.' and self._peek_char().isdigit():
            num_str += self._advance()
            while self._current_char().isdigit():
                num_str += self._advance()
        
        # Scientific notation (e or E)
        if self._current_char() in 'eE':
            num_str += self._advance()
            if self._current_char() in '+-':
                num_str += self._advance()
            while self._current_char().isdigit():
                num_str += self._advance()
        
        return Token(TokenType.NUMBER, num_str, start_line, start_column)
    
    def _read_string(self, quote: str) -> Token:
        """Read string literal"""
        start_line = self.line
        start_column = self.column
        string_val = ''
        
        self._advance()  # Skip opening quote
        
        # Handle triple quotes for Python
        if self.language == 'python' and self._current_char() == quote and self._peek_char() == quote:
            self._advance()
            self._advance()
            string_val = quote * 3
            
            while self.position < len(self.code):
                if (self._current_char() == quote and 
                    self._peek_char() == quote and 
                    self._peek_char(2) == quote):
                    string_val += self._advance()
                    string_val += self._advance()
                    string_val += self._advance()
                    break
                string_val += self._advance()
        else:
            string_val = quote
            
            while self.position < len(self.code) and self._current_char() != quote:
                if self._current_char() == '\\':
                    string_val += self._advance()
                    if self.position < len(self.code):
                        string_val += self._advance()
                else:
                    string_val += self._advance()
            
            if self._current_char() == quote:
                string_val += self._advance()
        
        return Token(TokenType.STRING, string_val, start_line, start_column)
    
    def _read_character(self) -> Token:
        """Read character literal (Java, C++)"""
        start_line = self.line
        start_column = self.column
        char_val = ''
        
        self._advance()  # Skip opening quote
        
        if self._current_char() == '\\':
            char_val += self._advance()
            if self.position < len(self.code):
                char_val += self._advance()
        else:
            char_val += self._advance()
        
        if self._current_char() == "'":
            char_val += self._advance()
        
        return Token(TokenType.CHARACTER, f"'{char_val}'", start_line, start_column)
    
    def _read_identifier(self) -> Token:
        """Read identifier or keyword"""
        start_line = self.line
        start_column = self.column
        ident = ''
        
        while (self._current_char().isalnum() or self._current_char() in '_'):
            ident += self._advance()
        
        # Check if it's a keyword
        if ident in self.keywords:
            return Token(TokenType.KEYWORD, ident, start_line, start_column)
        
        return Token(TokenType.IDENTIFIER, ident, start_line, start_column)
    
    def _read_comment(self) -> Token:
        """Read comment"""
        start_line = self.line
        start_column = self.column
        comment = ''
        
        # Single line comment
        if self._current_char() == '/' and self._peek_char() == '/':
            comment += self._advance()
            comment += self._advance()
            while self._current_char() != '\n' and self.position < len(self.code):
                comment += self._advance()
        
        # Multi-line comment or Python comment
        elif self._current_char() == '/' and self._peek_char() == '*':
            comment += self._advance()
            comment += self._advance()
            while self.position < len(self.code):
                if self._current_char() == '*' and self._peek_char() == '/':
                    comment += self._advance()
                    comment += self._advance()
                    break
                comment += self._advance()
        
        elif self._current_char() == '#':  # Python comment
            while self._current_char() != '\n' and self.position < len(self.code):
                comment += self._advance()
        
        return Token(TokenType.COMMENT, comment, start_line, start_column)
    
    def _read_operator(self) -> Token:
        """Read operator"""
        start_line = self.line
        start_column = self.column
        op = ''
        
        # Try to match longest operator first
        for length in [3, 2, 1]:
            test_op = self.code[self.position:self.position + length]
            if test_op in self.OPERATORS:
                op = test_op
                break
        
        if op:
            for _ in range(len(op)):
                self._advance()
        
        return Token(TokenType.OPERATOR, op, start_line, start_column) if op else None
    
    def _read_preprocessor(self) -> Token:
        """Read C++ preprocessor directive"""
        start_line = self.line
        start_column = self.column
        directive = ''
        
        while self._current_char() not in '\n\0':
            directive += self._advance()
        
        return Token(TokenType.PREPROCESSOR, directive, start_line, start_column)
    
    def tokenize(self, code: str) -> List[Dict]:
        """
        Tokenize source code
        
        Args:
            code: Source code to tokenize
        
        Returns:
            List of token dictionaries
        """
        self.code = code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        while self.position < len(self.code):
            self._skip_whitespace()
            
            if self.position >= len(self.code):
                break
            
            current = self._current_char()
            start_line = self.line
            start_column = self.column
            
            # Preprocessor directive (C++)
            if self.language == 'cpp' and current == '#':
                token = self._read_preprocessor()
                self.tokens.append(token)
            
            # Comments
            elif current == '/' and self._peek_char() in '/*':
                token = self._read_comment()
                self.tokens.append(token)
            
            elif self.language == 'python' and current == '#':
                token = self._read_comment()
                self.tokens.append(token)
            
            # Numbers
            elif current.isdigit():
                token = self._read_number()
                self.tokens.append(token)
            
            # Strings
            elif current in '"\'':
                token = self._read_string(current)
                self.tokens.append(token)
            
            # Character literals (Java, C++)
            elif self.language in ['java', 'cpp'] and current == "'":
                token = self._read_character()
                self.tokens.append(token)
            
            # Identifiers and keywords
            elif current.isalpha() or current == '_':
                token = self._read_identifier()
                self.tokens.append(token)
            
            # Operators
            elif current in '+-*/%=<>!&|^~':
                token = self._read_operator()
                if token:
                    self.tokens.append(token)
                else:
                    # Invalid operator
                    error_token = Token(TokenType.ERROR, current, start_line, start_column)
                    self.tokens.append(error_token)
                    self._advance()
            
            # Punctuation
            elif current in self.PUNCTUATION:
                token = Token(TokenType.PUNCTUATION, current, start_line, start_column)
                self.tokens.append(token)
                self._advance()
            
            # Unknown character
            else:
                error_token = Token(TokenType.ERROR, current, start_line, start_column)
                self.tokens.append(error_token)
                self._advance()
        
        # Convert tokens to dictionaries
        return [token.to_dict() for token in self.tokens]
