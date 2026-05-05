class Scanner:
    def __init__(self):
        self.code = {
            "A": [],
            "B": [],
        }

    def scan_codes(self, scan: str, columnActive: str):
        scan = scan[:-1]
        col = columnActive.upper()

        # scanner.py
        if scan not in self.code[col]:
            self.code[col].append(scan)
            return "added", scan
        else:
            return "duplicate", scan

    def get_codes(self):    
        return self.code

    def clear(self):
        self.code = {"A": [], "B": []}

    def count(self):
        return sum(len(v) for v in self.code.values())
