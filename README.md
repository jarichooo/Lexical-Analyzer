# Lexical Analyzer

A lightweight, reusable Python module for tokenizing source code in Python, Java, and C++. Perfect for code analysis, syntax highlighting, and compiler development.

## Overview

The Lexical Analyzer is a pure Python module that converts source code into a list of tokens with their types, values, and positions. It's designed to be imported and used in other Python scripts and applications.

## Features

- **Multi-Language Support**: Analyze Python, Java, and C++ code
- **Dictionary Output**: Tokens returned as dictionaries with type, value, line, and column information
- **Lexical Element Recognition**:
  - Keywords (language-specific)
  - Identifiers (variable and function names)
  - Literals (strings, numbers, booleans, characters)
  - Operators (arithmetic, logical, comparison, bitwise, assignment)
  - Punctuation symbols (brackets, braces, parentheses, semicolons)
  - Comments (single-line and block comments)
  - Preprocessor directives (C++ only)
- **Error Handling**: Detects and reports invalid tokens with line and column information
- **Precise Position Tracking**: Each token includes line and column numbers for easy debugging
- **Importable Module**: Use as a module in your own Python projects

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **Git** (optional, for cloning)

### Quick Setup

#### Windows
```bash
git clone https://github.com/jarichooo/Lexical-Analyzer.git
cd Lexical-Analyzer
python lexical_analyzer.py  # Just to verify it works
```

#### Linux (Ubuntu)
```bash
git clone https://github.com/jarichooo/Lexical-Analyzer.git
cd Lexical-Analyzer
python3 test_languages.py
```

#### Linux (Fedora)
```bash
git clone https://github.com/jarichooo/Lexical-Analyzer.git
cd Lexical-Analyzer
python3 test_languages.py
```

#### macOS
```bash
git clone https://github.com/jarichooo/Lexical-Analyzer.git
cd Lexical-Analyzer
python3 test_languages.py
```

## Usage

### Basic Import and Usage

```python
from lexical_analyzer import LexicalAnalyzer

# Create analyzer for Python
analyzer = LexicalAnalyzer('python')

# Tokenize code
code = "x = 42"
tokens = analyzer.tokenize(code)

# Use the tokens
for token in tokens:
    print(token)
```

### Output Example

```
{'type': 'IDENTIFIER', 'value': 'x', 'line': 1, 'column': 1}
{'type': 'OPERATOR', 'value': '=', 'line': 1, 'column': 3}
{'type': 'NUMBER', 'value': '42', 'line': 1, 'column': 5}
```

### Analyze Python Code

```python
from lexical_analyzer import LexicalAnalyzer

python_code = """
def greet(name):
    # This is a comment
    print(f"Hello, {name}!")
    x = 42
"""

analyzer = LexicalAnalyzer('python')
tokens = analyzer.tokenize(python_code)

for token in tokens:
    print(token)
```

### Analyze Java Code

```python
from lexical_analyzer import LexicalAnalyzer

java_code = """
public class Main {
    public static void main(String[] args) {
        int x = 10;
        System.out.println("Hello, World!");
    }
}
"""

analyzer = LexicalAnalyzer('java')
tokens = analyzer.tokenize(java_code)

for token in tokens:
    print(token)
```

### Analyze C++ Code

```python
from lexical_analyzer import LexicalAnalyzer

cpp_code = """
#include <iostream>
using namespace std;
int main() {
    int x = 0x1F;  // Hex number
    cout << "Hello, World!" << endl;
    return 0;
}
"""

analyzer = LexicalAnalyzer('cpp')
tokens = analyzer.tokenize(cpp_code)

for token in tokens:
    print(token)
```

## Running Tests

To test the analyzer with all three languages, run the test suite:

**Windows:**
```bash
python test_languages.py
```

**Linux/macOS:**
```bash
python3 test_languages.py
```

This will execute 6 comprehensive tests:
1. Python tokenization
2. Java tokenization
3. C++ tokenization
4. Error handling
5. Token filtering
6. Position tracking

## Processing Tokens

### Filter Tokens by Type

```python
analyzer = LexicalAnalyzer('python')
tokens = analyzer.tokenize("def add(a, b): return a + b")

# Get only keywords
keywords = [t for t in tokens if t['type'] == 'KEYWORD']

# Get only identifiers
identifiers = [t for t in tokens if t['type'] == 'IDENTIFIER']

# Get only operators
operators = [t for t in tokens if t['type'] == 'OPERATOR']

# Get errors (if any)
errors = [t for t in tokens if t['type'] == 'ERROR']
```

### Count Tokens by Type

```python
token_counts = {}
for token in tokens:
    token_type = token['type']
    token_counts[token_type] = token_counts.get(token_type, 0) + 1

for token_type, count in token_counts.items():
    print(f"{token_type}: {count}")
```

### Write Tokens to File

```python
import json

analyzer = LexicalAnalyzer('python')
tokens = analyzer.tokenize("x = 42")

# Save as JSON
with open('tokens.json', 'w') as f:
    json.dump(tokens, f, indent=2)
```

## Supported Languages

### Python
- **Keywords**: if, else, for, while, def, class, return, import, async, await, yield, etc.
- **String Literals**: Single quotes, double quotes, triple-quoted strings
- **Comments**: Single-line comments with `#`
- **Numbers**: Integers, floats, scientific notation
- **Identifiers**: Variable and function names with underscore support
- **Operators**: All Python operators including `**`, `//`, `@`, etc.

### Java
- **Keywords**: public, private, static, class, interface, extends, implements, final, abstract, etc.
- **String Literals**: Double-quoted strings with escape sequences
- **Character Literals**: Single-quoted characters
- **Comments**: Single-line (`//`) and multi-line (`/* */`)
- **Numbers**: Integers, floats, scientific notation
- **Type Annotations**: Full support for generic types and annotations
- **Operators**: All Java operators including `>>>`, `instanceof`, etc.

### C++
- **Keywords**: int, float, double, class, struct, template, virtual, inline, constexpr, etc.
- **String Literals**: Double-quoted strings with escape sequences
- **Character Literals**: Single-quoted characters
- **Comments**: Single-line (`//`) and multi-line (`/* */`)
- **Numbers**: Integers, floats, hex (`0x`), binary (`0b`), scientific notation
- **Preprocessor Directives**: `#include`, `#define`, `#ifdef`, etc.
- **Operators**: All C++ operators including scope resolution (`::`), arrow (`->`), etc.

## Token Types

The analyzer recognizes the following token types:

| Token Type | Description | Example |
|-----------|-------------|---------|
| `KEYWORD` | Language keywords | `if`, `class`, `def`, `public` |
| `IDENTIFIER` | Variable/function names | `x`, `myFunc`, `_private` |
| `NUMBER` | Numeric literals | `42`, `3.14`, `0xFF`, `0b1010` |
| `STRING` | String literals | `"hello"`, `'world'`, `"""text"""` |
| `CHARACTER` | Character literals | `'a'`, `'\n'` |
| `OPERATOR` | Operators | `+`, `-`, `==`, `->`, `::` |
| `PUNCTUATION` | Punctuation marks | `{`, `}`, `;`, `,`, `(`, `)` |
| `COMMENT` | Comments | `// comment`, `/* comment */`, `# comment` |
| `PREPROCESSOR` | C++ preprocessor directives | `#include`, `#define` |
| `ERROR` | Invalid/unrecognized tokens | Invalid characters or sequences |

## API Reference

### LexicalAnalyzer Class

#### Constructor
```python
LexicalAnalyzer(language: str)
```
- `language`: Programming language (`'python'`, `'java'`, or `'cpp'`)
- Raises `ValueError` if unsupported language is specified

#### Method: tokenize()
```python
tokenize(code: str) -> List[Dict]
```
- **Parameters**:
  - `code`: Source code string to tokenize
- **Returns**: List of token dictionaries
- **Each token dictionary contains**:
  - `type`: Token type (KEYWORD, IDENTIFIER, etc.)
  - `value`: The actual lexeme/text
  - `line`: Line number in source code (1-indexed)
  - `column`: Column number (1-indexed)

**Example:**
```python
analyzer = LexicalAnalyzer('python')
tokens = analyzer.tokenize("x = 42")
print(tokens)
# Output:
# [
#   {'type': 'IDENTIFIER', 'value': 'x', 'line': 1, 'column': 1},
#   {'type': 'OPERATOR', 'value': '=', 'line': 1, 'column': 3},
#   {'type': 'NUMBER', 'value': '42', 'line': 1, 'column': 5}
# ]
```

## Error Handling

The analyzer gracefully handles errors by:
- Creating tokens of type `ERROR` for unrecognized characters
- Including line and column information for error debugging
- Continuing tokenization after encountering errors
- Providing meaningful output for error analysis

**Example:**
```python
analyzer = LexicalAnalyzer('python')
tokens = analyzer.tokenize("x @ y")  # @ is not a Python operator

for token in tokens:
    if token['type'] == 'ERROR':
        print(f"Error at line {token['line']}, column {token['column']}: '{token['value']}'")
```

## Project Structure

```
Lexical-Analyzer/
├── README.md                  # Documentation (you are here)
├── CODE_EXPLANATION.md        # Detailed code explanation
├── lexical_analyzer.py        # Main lexical analyzer module
├── test_languages.py          # Comprehensive test suite
└── .gitignore                 # Git ignore file
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'lexical_analyzer'"
- **Solution**: Ensure `lexical_analyzer.py` is in the same directory as your script, or add it to your Python path

### "ValueError: Unsupported language"
- **Solution**: Use only `'python'`, `'java'`, or `'cpp'` as language parameter

### Position Numbers Don't Match My Editor
- **Note**: The analyzer uses 1-indexed line and column numbers (starting at 1), which is standard for error reporting

### Tokens Appear on Same Line
- **Note**: This is correct behavior. The analyzer properly tracks line numbers based on newline characters in the source code

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Use Cases

- **Code Analysis**: Analyze code structure and complexity
- **Syntax Highlighting**: Build syntax highlighters for IDEs
- **Code Formatters**: Create custom code formatters
- **Compiler Development**: First phase of compiler/interpreter development
- **Linters**: Build custom linters and static analysis tools
- **Educational**: Learn how lexical analysis works

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub: https://github.com/jarichooo/Lexical-Analyzer/issues
- Check the CODE_EXPLANATION.md for detailed documentation

## Author

Created by Joshua Jericho D. Barja

## Version History

### Version 1.0 (Current)
- Initial release
- Support for Python, Java, and C++
- Comprehensive token recognition
- Dictionary-based output format
- Error handling and position tracking
- Importable module design
- Comprehensive test suite
