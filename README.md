# Lexical Analyzer

A comprehensive lexical analyzer (tokenizer) for Python, Java, and C++ source code. This tool tokenizes source code and outputs tokens with their types as a list of dictionaries.

## Overview

This project provides a unified lexical analyzer that can tokenize source code from three popular programming languages: Python, Java, and C++. The analyzer recognizes lexical elements such as keywords, identifiers, literals, operators, and punctuation symbols, with comprehensive error handling and formatted output as dictionaries.

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

## Installation

### Prerequisites

- **Python 3.7 or higher** installed on your system
- **Git** (optional, for cloning the repository)

### Windows

#### Method 1: Using Git Bash or Command Prompt

1. **Open Command Prompt or PowerShell**
   - Press `Win + R`, type `cmd` or `powershell`, and press Enter

2. **Clone the repository**
   ```bash
   git clone https://github.com/jarichooo/Lexical-Analyzer.git
   cd Lexical-Analyzer
   ```

3. **Verify Python installation**
   ```bash
   python --version
   ```

4. **Run the lexical analyzer**
   ```bash
   python lexical_analyzer.py
   ```

#### Method 2: Manual Download

1. Visit https://github.com/jarichooo/Lexical-Analyzer
2. Click the green **Code** button
3. Click **Download ZIP**
4. Extract the ZIP file to your desired location
5. Open Command Prompt in the extracted folder
6. Run: `python lexical_analyzer.py`

### Linux (Ubuntu)

1. **Open Terminal** (Ctrl + Alt + T)

2. **Ensure Python 3 is installed**
   ```bash
   python3 --version
   ```
   
   If not installed, install it:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/jarichooo/Lexical-Analyzer.git
   cd Lexical-Analyzer
   ```

4. **Run the lexical analyzer**
   ```bash
   python3 lexical_analyzer.py
   ```

### Linux (Fedora)

1. **Open Terminal** (Ctrl + Alt + T)

2. **Ensure Python 3 is installed**
   ```bash
   python3 --version
   ```
   
   If not installed, install it:
   ```bash
   sudo dnf update
   sudo dnf install python3 python3-pip
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/jarichooo/Lexical-Analyzer.git
   cd Lexical-Analyzer
   ```

4. **Run the lexical analyzer**
   ```bash
   python3 lexical_analyzer.py
   ```

### macOS

1. **Open Terminal** (Command + Space, type "Terminal")

2. **Check if Python 3 is installed**
   ```bash
   python3 --version
   ```
   
   If not installed, install Python 3 using Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install python3
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/jarichooo/Lexical-Analyzer.git
   cd Lexical-Analyzer
   ```

4. **Run the lexical analyzer**
   ```bash
   python3 lexical_analyzer.py
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
- **Operators**: All C++ operators including `::`Scope resolution, `->`, `::`, etc.

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

## Running the Built-in Example

The `lexical_analyzer.py` file includes example code that demonstrates tokenization of Python, Java, and C++:

### Windows
```bash
python lexical_analyzer.py
```

### Linux/macOS
```bash
python3 lexical_analyzer.py
```

This will display tokens for sample Python, Java, and C++ code.

## API Reference

### LexicalAnalyzer Class

#### Constructor
```python
LexicalAnalyzer(language: str)
```
- `language`: Programming language ('python', 'java', or 'cpp')
- Raises `ValueError` if unsupported language is specified

#### Methods

**tokenize(code: str) -> List[Dict]**
- Tokenizes the provided source code
- Returns a list of token dictionaries
- Each dictionary contains: `type`, `value`, `line`, `column`

**Example:**
```python
analyzer = LexicalAnalyzer('python')
tokens = analyzer.tokenize("x = 42")
print(tokens)
# [{'type': 'IDENTIFIER', 'value': 'x', 'line': 1, 'column': 1}, ...]
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
├── lexical_analyzer.py        # Main lexical analyzer implementation
└── .gitignore                 # Git ignore file (if applicable)
```

## Troubleshooting

### "Python is not recognized as an internal or external command"
- **Windows**: Ensure Python is installed and added to PATH. Reinstall Python and check "Add Python to PATH"
- **Solution**: Use `python3` instead of `python` or reinstall with PATH setup

### "ModuleNotFoundError: No module named 'lexical_analyzer'"
- **Solution**: Ensure you're in the correct directory where `lexical_analyzer.py` is located
- Run: `cd Lexical-Analyzer` before importing

### "SyntaxError" when running the script
- **Solution**: Ensure you have Python 3.7 or higher
- Check: `python --version` or `python3 --version`

### Tokens appear on the same line
- **Note**: This is normal behavior. The analyzer correctly tracks line numbers in the source code
- Use the `line` and `column` values for precise positioning

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub: https://github.com/jarichooo/Lexical-Analyzer/issues
- Check existing documentation and examples

## Author

Created by Joshua Jericho D. Barja

## Version History

### Version 1.0 (Current)
- Initial release
- Support for Python, Java, and C++
- Comprehensive token recognition
- Dictionary-based output format
- Error handling and position tracking
