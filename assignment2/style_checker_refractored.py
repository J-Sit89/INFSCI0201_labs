import os
import ast
import re
from typing import List, Tuple


def get_file_path() -> str:
    """Prompt the user to enter the Python source file path."""
    return input("Enter the path to the Python file: ").strip()


def read_file(file_path: str) -> Tuple[str, List[str]]:
    """Read the content of a Python file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return ''.join(lines), lines


def analyze_file_structure(file_content: str) -> Tuple[int, List[str], List[str], List[str]]:
    """Analyze the file structure: total lines, imports, classes, and functions."""
    tree = ast.parse(file_content)
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    functions = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and not isinstance(node.parent, ast.ClassDef)
    ]
    return len(file_content.splitlines()), imports, classes, functions


def check_docstrings(tree: ast.AST) -> List[str]:
    """Check docstrings for classes and functions."""
    docstrings = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
            docstring = ast.get_docstring(node) or f"{node.name}: DocString not found."
            docstrings.append(f"{node.name}: {docstring}")
    return docstrings


def check_type_annotations(tree: ast.AST) -> List[str]:
    """Check for functions and methods missing type annotations."""
    unannotated = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not node.returns or any(arg.annotation is None for arg in node.args.args):
                unannotated.append(node.name)
    return unannotated


def check_naming_conventions(tree: ast.AST) -> Tuple[List[str], List[str]]:
    """Check naming conventions for classes and functions."""
    incorrect_classes = []
    incorrect_functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and not re.match(r'^[A-Z][a-zA-Z0-9]+$', node.name):
            incorrect_classes.append(node.name)
        elif isinstance(node, ast.FunctionDef) and not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
            incorrect_functions.append(node.name)
    return incorrect_classes, incorrect_functions


def generate_report(file_name: str, file_path: str, file_content: str, analysis_results: dict) -> None:
    """Generate a report and save it to a file."""
    report_path = os.path.join(os.path.dirname(file_path), f"style_report_{file_name}.txt")
    with open(report_path, 'w') as report:
        report.write("File Structure:\n")
        report.write(f"Total lines: {analysis_results['total_lines']}\n")
        report.write(f"Imports: {', '.join(analysis_results['imports'])}\n")
        report.write(f"Classes: {', '.join(analysis_results['classes'])}\n")
        report.write(f"Functions: {', '.join(analysis_results['functions'])}\n\n")

        report.write("DocStrings:\n")
        report.write('\n\n'.join(analysis_results['docstrings']) + '\n\n')

        report.write("Type Annotation Check:\n")
        if analysis_results['unannotated']:
            report.write(f"Unannotated functions/methods: {', '.join(analysis_results['unannotated'])}\n")
        else:
            report.write("All functions and methods have type annotations.\n")

        report.write("Naming Convention Check:\n")
        if analysis_results['incorrect_classes']:
            report.write(f"Incorrect Class Names: {', '.join(analysis_results['incorrect_classes'])}\n")
        if analysis_results['incorrect_functions']:
            report.write(f"Incorrect Function Names: {', '.join(analysis_results['incorrect_functions'])}\n")
        if not analysis_results['incorrect_classes'] and not analysis_results['incorrect_functions']:
            report.write("All names adhere to naming conventions.\n")


def main():
    file_path = get_file_path()
    file_content, lines = read_file(file_path)
    tree = ast.parse(file_content)

    # Functional processing
    total_lines, imports, classes, functions = analyze_file_structure(file_content)
    docstrings = check_docstrings(tree)
    unannotated = check_type_annotations(tree)
    incorrect_classes, incorrect_functions = check_naming_conventions(tree)

    # Generate analysis results
    analysis_results = {
        "total_lines": total_lines,
        "imports": imports,
        "classes": classes,
        "functions": functions,
        "docstrings": docstrings,
        "unannotated": unannotated,
        "incorrect_classes": incorrect_classes,
        "incorrect_functions": incorrect_functions,
    }

    # Generate the report
    generate_report(os.path.basename(file_path).replace('.py', ''), file_path, file_content, analysis_results)


if __name__ == "__main__":
    main()
