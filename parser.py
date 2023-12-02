import re

class TPPParser:
    def __init__(self):
        self.variables = {}

    def parse(self, code):
        # Split code into lines
        lines = code.split(';')

        for line in lines:
            line = line.strip()
            if line:
                self.parse_line(line)

    def parse_line(self, line):
        if re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*\s*=\s*\d+', line):  # Variable assignment
            variable, value = line.split('=')
            variable = variable.strip()
            value = int(value.strip())
            self.variables[variable] = value
        elif re.match(r'^print\(.+\)', line):  # Print statement
            expression = re.search(r'\((.+)\)', line).group(1)
            value = self.evaluate_expression(expression)
            print(value)
        else:
            print(f"Syntax Error: {line}")

    def evaluate_expression(self, expression):
        # For simplicity, assuming expressions are simple arithmetic expressions
        return eval(expression, {}, self.variables)

# Example code in your custom language
custom_code = """
a = 10;
b = 20;
print(a + b);
"""

parser = TPPParser()
parser.parse(custom_code)
