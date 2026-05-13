"""
Test file for the Lexical Analyzer
Tests tokenization for Python, Java, and C++ code
"""

from lexical_analyzer import LexicalAnalyzer
import json


def test_python():
    """Test Python code tokenization"""
    print("=" * 80)
    print("TESTING PYTHON TOKENIZATION")
    print("=" * 80)
    
    python_code = """
def greet(name):
    # This is a comment
    print(f"Hello, {name}!")
    x = 42
    y = 3.14
    """
    
    analyzer = LexicalAnalyzer('python')
    tokens = analyzer.tokenize(python_code)
    
    print(f"\nCode:\n{python_code}")
    print(f"\nTokens ({len(tokens)} total):")
    print("-" * 80)
    
    for i, token in enumerate(tokens, 1):
        print(f"{i:3}. {token}")
    
    # Count by type
    token_types = {}
    for token in tokens:
        token_type = token['type']
        token_types[token_type] = token_types.get(token_type, 0) + 1
    
    print(f"\nToken Type Summary:")
    print("-" * 80)
    for token_type, count in sorted(token_types.items()):
        print(f"{token_type:15} : {count:3} tokens")
    
    return tokens


def test_java():
    """Test Java code tokenization"""
    print("\n" + "=" * 80)
    print("TESTING JAVA TOKENIZATION")
    print("=" * 80)
    
    java_code = """
public class Main {
    public static void main(String[] args) {
        int x = 10;
        double y = 3.14;
        System.out.println("Hello, World!");
    }
}
    """
    
    analyzer = LexicalAnalyzer('java')
    tokens = analyzer.tokenize(java_code)
    
    print(f"\nCode:\n{java_code}")
    print(f"\nTokens ({len(tokens)} total):")
    print("-" * 80)
    
    for i, token in enumerate(tokens, 1):
        print(f"{i:3}. {token}")
    
    # Count by type
    token_types = {}
    for token in tokens:
        token_type = token['type']
        token_types[token_type] = token_types.get(token_type, 0) + 1
    
    print(f"\nToken Type Summary:")
    print("-" * 80)
    for token_type, count in sorted(token_types.items()):
        print(f"{token_type:15} : {count:3} tokens")
    
    return tokens


def test_cpp():
    """Test C++ code tokenization"""
    print("\n" + "=" * 80)
    print("TESTING C++ TOKENIZATION")
    print("=" * 80)
    
    cpp_code = """
#include <iostream>
using namespace std;

int main() {
    int x = 0x1F;  // Hex number
    int y = 0b1010;  // Binary number
    double z = 1.5e-10;  // Scientific notation
    cout << "Hello, World!" << endl;
    return 0;
}
    """
    
    analyzer = LexicalAnalyzer('cpp')
    tokens = analyzer.tokenize(cpp_code)
    
    print(f"\nCode:\n{cpp_code}")
    print(f"\nTokens ({len(tokens)} total):")
    print("-" * 80)
    
    for i, token in enumerate(tokens, 1):
        print(f"{i:3}. {token}")
    
    # Count by type
    token_types = {}
    for token in tokens:
        token_type = token['type']
        token_types[token_type] = token_types.get(token_type, 0) + 1
    
    print(f"\nToken Type Summary:")
    print("-" * 80)
    for token_type, count in sorted(token_types.items()):
        print(f"{token_type:15} : {count:3} tokens")
    
    return tokens


def test_error_handling():
    """Test error handling in tokenization"""
    print("\n" + "=" * 80)
    print("TESTING ERROR HANDLING")
    print("=" * 80)
    
    # Code with errors
    error_code = "x @ y = 42"
    
    analyzer = LexicalAnalyzer('python')
    tokens = analyzer.tokenize(error_code)
    
    print(f"\nCode with error:\n{error_code}")
    print(f"\nTokens ({len(tokens)} total):")
    print("-" * 80)
    
    for i, token in enumerate(tokens, 1):
        status = "✗ ERROR" if token['type'] == 'ERROR' else "✓ OK"
        print(f"{i:3}. {status:10} {token}")
    
    # Find errors
    errors = [t for t in tokens if t['type'] == 'ERROR']
    print(f"\nErrors found: {len(errors)}")
    for error in errors:
        print(f"  - '{error['value']}' at line {error['line']}, column {error['column']}")
    
    return tokens


def test_token_filtering():
    """Test filtering tokens by type"""
    print("\n" + "=" * 80)
    print("TESTING TOKEN FILTERING")
    print("=" * 80)
    
    python_code = """
def add(a, b):
    return a + b
result = add(5, 10)
    """
    
    analyzer = LexicalAnalyzer('python')
    tokens = analyzer.tokenize(python_code)
    
    print(f"\nCode:\n{python_code}")
    
    # Filter by type
    keywords = [t for t in tokens if t['type'] == 'KEYWORD']
    identifiers = [t for t in tokens if t['type'] == 'IDENTIFIER']
    numbers = [t for t in tokens if t['type'] == 'NUMBER']
    operators = [t for t in tokens if t['type'] == 'OPERATOR']
    
    print(f"\nFiltered Tokens:")
    print("-" * 80)
    print(f"\nKeywords ({len(keywords)}):")
    for token in keywords:
        print(f"  - {token['value']}")
    
    print(f"\nIdentifiers ({len(identifiers)}):")
    for token in identifiers:
        print(f"  - {token['value']}")
    
    print(f"\nNumbers ({len(numbers)}):")
    for token in numbers:
        print(f"  - {token['value']}")
    
    print(f"\nOperators ({len(operators)}):")
    for token in operators:
        print(f"  - {token['value']}")
    
    return tokens


def test_position_tracking():
    """Test line and column tracking"""
    print("\n" + "=" * 80)
    print("TESTING POSITION TRACKING")
    print("=" * 80)
    
    python_code = """x = 42
y = 3.14
z = x + y"""
    
    analyzer = LexicalAnalyzer('python')
    tokens = analyzer.tokenize(python_code)
    
    print(f"\nCode:\n{python_code}")
    print(f"\nTokens with Position Information:")
    print("-" * 80)
    print(f"{'#':>3} {'Type':<15} {'Value':<15} {'Line':<5} {'Column':<5}")
    print("-" * 80)
    
    for i, token in enumerate(tokens, 1):
        print(f"{i:3} {token['type']:<15} {token['value']:<15} {token['line']:<5} {token['column']:<5}")
    
    return tokens


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "LEXICAL ANALYZER TEST SUITE" + " " * 31 + "║")
    print("╚" + "=" * 78 + "╝")
    
    # Run tests
    test_python()
    test_java()
    test_cpp()
    test_error_handling()
    test_token_filtering()
    test_position_tracking()
    
    print("\n" + "=" * 80)
    print("ALL TESTS COMPLETED")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
