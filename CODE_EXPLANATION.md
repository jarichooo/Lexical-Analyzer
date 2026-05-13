# Code Explanation: Lexical Analyzer

This document provides a detailed explanation of how the lexical analyzer code works, breaking down each component and explaining the logic behind the implementation.

## Table of Contents

1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [Class Structure](#class-structure)
4. [Detailed Component Breakdown](#detailed-component-breakdown)
5. [Tokenization Process](#tokenization-process)
6. [Language-Specific Handling](#language-specific-handling)
7. [Error Handling](#error-handling)
8. [Example Walkthrough](#example-walkthrough)

---

## Overview

The lexical analyzer is a Python-based tool that breaks down source code into tokens. It works like a scanner that reads code character by character and groups them into meaningful units (tokens) such as keywords, identifiers, numbers, strings, operators, and punctuation.

**Key Purpose**: Convert raw source code into a structured list of tokens with metadata (type, value, line number, column number).

---

## Core Concepts

### What is a Token?

A **token** is the smallest meaningful unit in source code. For example:

```python
x = 42
```

This line breaks down into 3 tokens:
- `x` → Identifier token
- `=` → Operator token
- `42` → Number token

### What is Lexical Analysis?

**Lexical analysis** is the process of converting a sequence of characters into a sequence of tokens. It's the first phase of compilation/interpretation.

### Token Types

The analyzer recognizes 10 different token types:

1. **KEYWORD** - Reserved words (if, while, class, public, etc.)
2. **IDENTIFIER** - Variable/function names
3. **NUMBER** - Numeric literals (integers, floats, hex, binary)
4. **STRING** - String literals (quoted text)
5. **CHARACTER** - Single character literals (Java, C++)
6. **OPERATOR** - Mathematical/logical operators (+, -, ==, &&, etc.)
7. **PUNCTUATION** - Symbols like brackets, semicolons, parentheses
8. **COMMENT** - Code comments
9. **PREPROCESSOR** - C++ preprocessor directives (#include, #define)
10. **ERROR** - Invalid/unrecognized tokens

---

## Class Structure

The code has two main classes:

### 1. Token Class

```python
class Token:
    """Represents a single token"""
    def __init__(self, type_: TokenType, value: str, line: int, column: int):
        self.type = type_          # Token type (KEYWORD, IDENTIFIER, etc.)
        self.value = value         # The actual text of the token
        self.line = line           # Line number where token appears
        self.column = column       # Column number where token starts
```

**Purpose**: Encapsulates all information about a single token.

**Key Methods**:
- `to_dict()` - Converts token to dictionary format for output
- `__repr__()` - Provides readable string representation

### 2. LexicalAnalyzer Class

```python
class LexicalAnalyzer:
    """Main lexical analyzer supporting Python, Java, and C++"""
```

**Purpose**: The main analyzer that tokenizes source code.

**Key Attributes**:
- Language-specific keyword sets (PYTHON_KEYWORDS, JAVA_KEYWORDS, CPP_KEYWORDS)
- Operator and punctuation definitions
- Current position, line, and column tracking during tokenization

---

## Detailed Component Breakdown

### 1. Keyword Sets

```python
PYTHON_KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    ...
}

JAVA_KEYWORDS = {
    'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch',
    'char', 'class', 'const', 'continue', 'default', 'do', 'double',
    ...
}

CPP_KEYWORDS = {
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel',
    ...
}
```

**Why Separate Sets?**
Each language has different reserved words. By maintaining separate sets, we can quickly check if a word is a keyword in the target language.

**Example**:
- `class` is a keyword in all three languages ✓
- `async` is a keyword in Python and C++, but not Java
- `public` is a keyword in Java and C++, but not Python

### 2. Operators and Punctuation

```python
OPERATORS = {
    '+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
    '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', ...
}

PUNCTUATION = {
    '(', ')', '{', '}', '[', ']', ';', ',', '.', '@', '#', '$'
}
```

**Why Store Them?**
These are static and shared across all three languages, so we store them once for quick lookup.

### 3. Position Tracking Variables

```python
self.position = 0      # Current position in the code string
self.line = 1          # Current line number
self.column = 1        # Current column number
self.code = ""         # The source code being analyzed
self.tokens = []       # List of tokens found
```

**Why Track Position?**
Each token needs to know where it appears in the source code. This is crucial for:
- Error reporting with exact location
- Debugging
- Mapping tokens back to source

---

## Detailed Component Breakdown (Helper Methods)

### Character Navigation Methods

#### `_current_char()`
```python
def _current_char(self) -> str:
    """Get current character"""
    if self.position >= len(self.code):
        return '\0'
    return self.code[self.position]
```

**Purpose**: Returns the character at the current position without advancing.
**Returns**: The current character or null character `\0` if at end.

#### `_peek_char(offset=1)`
```python
def _peek_char(self, offset: int = 1) -> str:
    """Peek ahead at character"""
    pos = self.position + offset
    if pos >= len(self.code):
        return '\0'
    return self.code[pos]
```

**Purpose**: Look ahead to see the next character(s) without advancing.
**Usage**: When deciding if `=` is an assignment operator or part of `==`.

#### `_advance()`
```python
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
```

**Purpose**: Move to the next character and track line/column.
**Smart Handling**: When a newline is encountered, it resets the column and increments the line.

---

## Tokenization Process

### Main Method: `tokenize(code: str)`

```python
def tokenize(self, code: str) -> List[Dict]:
    """Tokenize source code and return list of token dictionaries"""
    self.code = code
    self.position = 0
    self.line = 1
    self.column = 1
    self.tokens = []
    
    while self.position < len(self.code):
        self._skip_whitespace()
        
        if self.position >= len(self.code):
            break
        
        # ... process tokens based on current character
```

**Flow**:
1. Reset all tracking variables
2. Loop through every character
3. Skip whitespace (not part of tokens)
4. Identify what type of token is starting
5. Call appropriate method to read that token
6. Add token to list
7. Continue until end of code

### Step-by-Step Process

Let's trace through: `x = 42`

```
Position: 0, Char: 'x'
├─ Is alphanumeric? YES
├─ Call _read_identifier()
├─ Reads: "x"
├─ Check if keyword? NO
└─ Create IDENTIFIER token: {'type': 'IDENTIFIER', 'value': 'x', 'line': 1, 'column': 1}

Position: 1, Char: ' '
├─ Is whitespace? YES
└─ Call _skip_whitespace()

Position: 2, Char: '='
├─ Is operator? YES
├─ Call _read_operator()
├─ Reads: "="
└─ Create OPERATOR token: {'type': 'OPERATOR', 'value': '=', 'line': 1, 'column': 3}

Position: 3, Char: ' '
├─ Is whitespace? YES
└─ Call _skip_whitespace()

Position: 4, Char: '4'
├─ Is digit? YES
├─ Call _read_number()
├─ Reads: "42"
└─ Create NUMBER token: {'type': 'NUMBER', 'value': '42', 'line': 1, 'column': 5}

Position: 6 (end of string)
└─ Exit loop
```

**Result**:
```python
[
    {'type': 'IDENTIFIER', 'value': 'x', 'line': 1, 'column': 1},
    {'type': 'OPERATOR', 'value': '=', 'line': 1, 'column': 3},
    {'type': 'NUMBER', 'value': '42', 'line': 1, 'column': 5}
]
```

---

## Language-Specific Handling

### 1. Number Reading (`_read_number()`)

```python
def _read_number(self) -> Token:
    # Handle hex, binary, octal (C++ only)
    if self.language == 'cpp' and self._current_char() == '0':
        if self._peek_char() == 'x':
            # Hexadecimal: 0xFF
        elif self._peek_char() == 'b':
            # Binary: 0b1010
    
    # Regular decimal number
    while self._current_char().isdigit():
        num_str += self._advance()
    
    # Decimal point
    if self._current_char() == '.' and self._peek_char().isdigit():
        num_str += self._advance()
        while self._current_char().isdigit():
            num_str += self._advance()
    
    # Scientific notation (e.g., 1.5e-10)
    if self._current_char() in 'eE':
        ...
```

**Why Different?**
- **C++**: Supports hex (`0xFF`), binary (`0b1010`), which Python and Java don't emphasize
- **Python**: Supports scientific notation like `1e10`
- **Java**: Similar to Python's number format

### 2. String Reading (`_read_string()`)

```python
def _read_string(self, quote: str) -> Token:
    # Python allows triple quotes
    if self.language == 'python' and self._current_char() == quote and self._peek_char() == quote:
        # Handle triple-quoted strings
        while not (found triple closing quotes):
            string_val += self._advance()
    else:
        # Standard single or double quoted string
        while self._current_char() != quote:
            if self._current_char() == '\\':
                # Handle escape sequences
                string_val += self._advance()
                string_val += self._advance()
            else:
                string_val += self._advance()
```

**Language Differences**:
- **Python**: Supports `"""triple quotes"""` for multi-line strings
- **Java/C++**: Standard double-quoted strings only
- **All**: Support escape sequences like `\n`, `\"`, `\\`

### 3. Comment Reading (`_read_comment()`)

```python
def _read_comment(self) -> Token:
    if self._current_char() == '/' and self._peek_char() == '/':
        # Single-line comment: read until newline
        while self._current_char() != '\n':
            comment += self._advance()
    
    elif self._current_char() == '/' and self._peek_char() == '*':
        # Multi-line comment: read until */
        while not (found '*/'):
            comment += self._advance()
    
    elif self._current_char() == '#':  # Python
        # Python comment: read until newline
        while self._current_char() != '\n':
            comment += self._advance()
```

**Language Differences**:
- **Python**: Uses `#` for comments
- **Java/C++**: Use `//` for single-line and `/* */` for multi-line

---

## Error Handling

### Error Detection

```python
else:
    # Unknown character
    error_token = Token(TokenType.ERROR, current, start_line, start_column)
    self.tokens.append(error_token)
    self._advance()
```

**When Errors Occur**:
1. An unrecognized character is encountered
2. A token cannot be properly parsed
3. An incomplete token (e.g., unclosed string)

**How Handled**:
- Create an ERROR token with the problematic character
- Include line and column for debugging
- Continue analyzing the rest of the code
- The error token appears in the output so users can see what went wrong

**Example**:
```python
code = "x @ y"  # @ is not a Python operator
tokens = analyzer.tokenize(code)
# Output includes:
# {'type': 'ERROR', 'value': '@', 'line': 1, 'column': 3}
```

---

## Example Walkthrough

### Complete Example: Python Function

**Input Code**:
```python
def greet(name):
    print("Hello")
```

**Tokenization Process**:

```
Line 1: "def greet(name):"
├─ "def" → Check keywords → KEYWORD
├─ "greet" → IDENTIFIER
├─ "(" → PUNCTUATION
├─ "name" → IDENTIFIER
├─ ")" → PUNCTUATION
├─ ":" → PUNCTUATION

Line 2: "    print("Hello")"
├─ Skip 4 spaces (whitespace)
├─ "print" → IDENTIFIER (not a keyword)
├─ "(" → PUNCTUATION
├─ ""Hello"" → STRING
├─ ")" → PUNCTUATION
```

**Output**:
```python
[
    {'type': 'KEYWORD', 'value': 'def', 'line': 1, 'column': 1},
    {'type': 'IDENTIFIER', 'value': 'greet', 'line': 1, 'column': 5},
    {'type': 'PUNCTUATION', 'value': '(', 'line': 1, 'column': 10},
    {'type': 'IDENTIFIER', 'value': 'name', 'line': 1, 'column': 11},
    {'type': 'PUNCTUATION', 'value': ')', 'line': 1, 'column': 15},
    {'type': 'PUNCTUATION', 'value': ':', 'line': 1, 'column': 16},
    {'type': 'IDENTIFIER', 'value': 'print', 'line': 2, 'column': 5},
    {'type': 'PUNCTUATION', 'value': '(', 'line': 2, 'column': 10},
    {'type': 'STRING', 'value': '"Hello"', 'line': 2, 'column': 11},
    {'type': 'PUNCTUATION', 'value': ')', 'line': 2, 'column': 18}
]
```

---

## Key Insights

### 1. **Why Use Separate Language Keyword Sets?**
Different languages have different reserved words. This allows the analyzer to correctly identify keywords for each language without confusion.

### 2. **Why Track Line and Column?**
When errors occur or you need to debug, knowing exactly where in the source code a token appears is invaluable.

### 3. **Why Read Tokens Instead of Using Regex?**
- Regex can be complex for handling all edge cases
- Character-by-character reading gives precise control
- Line and column tracking is easier to implement
- Error handling is more granular

### 4. **Why Handle Different Number Formats?**
Different languages support different number formats:
- Python: `1e10` (scientific notation)
- C++: `0xFF` (hex), `0b1010` (binary)
- Java: Similar to Python

### 5. **Why Continue After Errors?**
By continuing tokenization after errors, we can find multiple errors in one pass, giving developers complete feedback instead of stopping at the first error.

---

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Tokenize | O(n) | O(n) |
| _read_identifier | O(k) | O(k) |
| _read_number | O(k) | O(k) |
| _read_string | O(k) | O(k) |
| _read_comment | O(k) | O(k) |

Where:
- `n` = length of source code
- `k` = length of individual token

---

## Summary

The lexical analyzer works by:

1. **Reading** the source code character by character
2. **Identifying** what type of token is starting based on the current character
3. **Reading** the complete token using language-specific rules
4. **Tracking** the token's type, value, line, and column
5. **Storing** the token in a list
6. **Repeating** until the end of the code

The result is a structured list of tokens that can be used for:
- **Parsing** (converting to an Abstract Syntax Tree)
- **Compilation** (further processing)
- **Interpretation** (execution)
- **Analysis** (checking code structure)
- **Error reporting** (identifying syntax errors with exact locations)

