class ColumnSelector:
    def __init__(self):
        self.column_list = ["A", "B"]
        self.active_column = "A"

    def switch_column(self, columnActive: str):
        columnActive = columnActive.upper().strip()

        if columnActive in self.column_list:
            self.active_column = columnActive
            return True
        else:
            return False

    def get_active_column(self):
        return self.active_column
