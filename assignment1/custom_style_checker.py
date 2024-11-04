import ast
import os
import re

class StyleChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.report_data = {
            "file_structure": {},
            "docstrings": [],
            "type_annotations": [],
            "naming_conventions": []
        }
        
    def analyze_file_structure(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        
        self.report_data["file_structure"]["total_lines"] = len(content.splitlines())
    
        tree = ast.parse(content)
        imports, classes, functions = [], [], []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                imports.extend([n.name for n in node.names])
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)
        
        self.report_data["file_structure"]["imports"] = imports
        self.report_data["file_structure"]["classes"] = classes
        self.report_data["file_structure"]["functions"] = functions
    
    def check_docstrings(self):
        with open(self.file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                if docstring:
                    self.report_data["docstrings"].append(f"{node.name}: {docstring}")
                else:
                    self.report_data["docstrings"].append(f"{node.name}: DocString not found.")
    
    def check_type_annotations(self):
        with open(self.file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                has_annotation = bool(node.returns or any(arg.annotation for arg in node.args.args))
                if not has_annotation:
                    self.report_data["type_annotations"].append(f"{node.name} lacks type annotations.")
        
        if not self.report_data["type_annotations"]:
            self.report_data["type_annotations"].append("All functions and methods have type annotations.")
    
    def check_naming_conventions(self):
        camel_case = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
        snake_case = re.compile(r'^[a-z_][a-z0-9_]*$')
        
        for class_name in self.report_data["file_structure"]["classes"]:
            if not camel_case.match(class_name):
                self.report_data["naming_conventions"].append(f"Class '{class_name}' does not follow CamelCase.")
        
        for func_name in self.report_data["file_structure"]["functions"]:
            if not snake_case.match(func_name):
                self.report_data["naming_conventions"].append(f"Function '{func_name}' does not follow snake_case.")
        
        if not self.report_data["naming_conventions"]:
            self.report_data["naming_conventions"].append("All names adhere to the specified naming conventions.")
    
    def generate_report(self):
        file_name = os.path.basename(self.file_path).replace('.py', '')
        report_file = f"style_report_{file_name}.txt"
        
        with open(report_file, 'w') as file:
            file.write("File Structure:\n")
            file.write(f"Total Lines: {self.report_data['file_structure']['total_lines']}\n")
            file.write(f"Imports: {', '.join(self.report_data['file_structure']['imports'])}\n")
            file.write(f"Classes: {', '.join(self.report_data['file_structure']['classes'])}\n")
            file.write(f"Functions: {', '.join(self.report_data['file_structure']['functions'])}\n\n")
            
            file.write("DocStrings:\n")
            for doc in self.report_data["docstrings"]:
                file.write(f"{doc}\n\n")
            
            file.write("Type Annotations:\n")
            for annotation in self.report_data["type_annotations"]:
                file.write(f"{annotation}\n")
            
            file.write("\nNaming Conventions:\n")
            for convention in self.report_data["naming_conventions"]:
                file.write(f"{convention}\n")
        
        print(f"Report generated: {report_file}")

    def run_checks(self):
        self.analyze_file_structure()
        self.check_docstrings()
        self.check_type_annotations()
        self.check_naming_conventions()
        self.generate_report()

# Example usage
file_path = "C:/Users/jjsit/OneDrive/Desktop/INFSCI0201_labs-main/lab01/unitconverter.py"  # Replace with the path to the Python file you want to check
checker = StyleChecker(file_path)
checker.run_checks()
