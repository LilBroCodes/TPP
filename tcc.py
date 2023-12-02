import ast
from parser import TPPParser


def open_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except PermissionError:
        print(f"Permission denied: {filename}")
        return None
    except Exception as e:
        print(e)
        return None


class TCC:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        parsed_code = TPPParser().parse(code)
        self.visit(parsed_code)

    def visit(self, node):
        method_name = f"visit_{node.__class__.__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)
            elif isinstance(value, ast.AST):
                self.visit(value)

    def visit_Assign(self, node):
        target = node.targets[0].id
        value = self.visit(node.value)
        self.variables[target] = value

    def visit_Num(self, node):
        return node.n

    def visit_Str(self, node):
        return node.s

    def visit_Name(self, node):
        return self.variables[node.id]

    def visit_Print(self, node):
        for item in node.values:
            value = self.visit(item)
            print(value)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.op.__class__.__name__
        if op == "Add":
            return left + right
        elif op == "Sub":
            return left - right
        elif op == "Mult":
            return left * right
        elif op == "Div":
            return left / right
