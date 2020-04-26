"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:
    
    def __init__(self):
        self.table = dict()
        
    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """
    def insert(self, row_key, column_key, value):
        newCol = Column(column_key, value)
        if row_key not in self.table:
            self.table[row_key] = []
        
        row = self.table[row_key]
        for col in row:
            if col.key == column_key:
                col.value = value 
                return 
        row.append(newCol)
        row.sort(key=lambda col:col.key)
        return 
        

    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, row_key, column_start, column_end):
        if row_key not in self.table:
            return []
        result = []
        row = self.table[row_key]
        for col in row:
            key = col.key
            if column_start <= key <= column_end:
                result.append(col)
        return result