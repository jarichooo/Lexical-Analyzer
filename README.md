# Lexical Analyzer

A comprehensive lexical analyzer (tokenizer) for Python, Java, and C++ source code.

## Overview

This project provides a unified lexical analyzer that can tokenize source code from three popular programming languages: Python, Java, and C++. The analyzer recognizes lexical elements such as keywords, identifiers, literals, operators, and punctuation symbols, with comprehensive error handling and formatted output.

## Features

- **Multi-Language Support**: Analyze Python, Java, and C++ code
- **Lexical Element Recognition**:
  - Keywords
  - Identifiers
  - Literals (strings, numbers, booleans)
  - Operators
  - Punctuation symbols
  - Comments
- **Error Handling**: Detects and reports invalid tokens with line and column information
- **Formatted Output**: Provides a list of tokens with type, value, and position information
- **Unit Tests**: Comprehensive test coverage for all supported languages

## Project Structure

```
Lexical-Analyzer/
├── README.md
├── token.py                  # Token class definition
├── lexical_analyzer.py       # Core lexical analyzer
├── languages/
│   ├── python_lexer.py      # Python-specific lexer
│   ├── java_lexer.py        # Java-specific lexer
│   └── cpp_lexer.py         # C++-specific lexer
├── tests/
│   ├── test_python.py       # Python lexer tests
│   ├── test_java.py         # Java lexer tests
│   └── test_cpp.py          # C++ lexer tests
├── examples/
│   ├── sample.py            # Python example
│   ├── Sample.java          # Java example
│   └── sample.cpp           # C++ example
└── main.py                  # Main entry point with usage examples
```

## Installation

```bash
git clone https://github.com/jarichooo/Lexical-Analyzer.git
cd Lexical-Analyzer
```

## Usage

### Basic Usage

```python
from lexical_analyzer import LexicalAnalyzer

# Create analyzer for Python
analyzer = LexicalAnalyzer('python')

# Tokenize code
code = "x = 42"
tokens = analyzer.tokenize(code)

# Display tokens
for token in tokens:
    print(token)
```

### Output Example

```
Token(type=IDENTIFIER, value='x', line=1, column=1)
Token(type=OPERATOR, value='=', line=1, column=3)
Token(type=NUMBER, value='42', line=1, column=5)
```

## Supported Languages

### Python
- Keywords: if, else, for, while, def, class, return, import, etc.
- String literals: single, double, triple quotes
- Comments: # for single-line comments
- Indentation handling

### Java
- Keywords: public, private, static, class, interface, extends, implements, etc.
- String and character literals
- Comments: // for single-line, /* */ for multi-line
- Generics support

### C++
- Keywords: int, float, double, class, struct, template, virtual, etc.
- String and character literals
- Comments: // for single-line, /* */ for multi-line
- Preprocessor directives (#include, #define, etc.)

## Running Tests

```bash
python -m pytest tests/
```

## Token Types

- `KEYWORD`: Language keywords
- `IDENTIFIER`: Variable/function names
- `NUMBER`: Numeric literals (int, float)
- `STRING`: String literals
- `CHARACTER`: Character literals (C++, Java)
- `OPERATOR`: Operators (+, -, *, /, =, ==, !=, etc.)
- `PUNCTUATION`: Punctuation marks ({, }, (, ), [, ], ;, :, etc.)
- `COMMENT`: Comments
- `ERROR`: Invalid tokens

## Error Handling

The analyzer tracks errors with line and column numbers for easy debugging:

```python
tokens, errors = analyzer.tokenize_with_errors(code)
for error in errors:
    print(f"Error at line {error['line']}, column {error['column']}: {error['message']}")
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License
