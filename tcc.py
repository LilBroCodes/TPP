import re

class TppReader:
    def __init__(self):
        pass

    def get_set(self, line):
        pattern = r'^(.*?)\s*=\s*(.*?)(;)?$'
        match = re.match(pattern, line)
        if match:
            var_name = match.group(1)
            data = match.group(2)
            if data.startswith('"') and data.endswith('"'):
                data = data[1:-1]
            elif data.startswith("'") and data.endswith("'"):
                data = data[1:-1]
            else:
                data = int(data)
            return var_name, data
        else:
            raise ValueError("Invalid line format.")

    def open_tpp(self, filename: str, version="p"):
        if not filename:
            raise ValueError("Filename not supplied, expected str, got None instead.")
        if not version == "p":
            raise ValueError(f'Python compiler can only read files, with version "p", got {version} instead.')

        with open(filename, "r") as file:
            data = file.read()

            lines = data.split('\n')

        return lines

    def check_function(self, line) -> str or None:
        match = re.match(r'^(.*?)\((.*?)\);$')
        if match:
            return match.group(1)
        else:
            return None

    def check_args(self, line, function) -> list or tuple:
        pattern = r"^(.*);"
        match = re.match(pattern, line)
        if not match or function not in line:
            raise ValueError("Function not in line, or missing ';'.")

        return match.group(1)
