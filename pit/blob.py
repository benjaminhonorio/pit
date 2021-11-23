class Blob:
    oid = None
    
    def __init__(self, data):
        self.data = data
    
    def type(self):
        return 'blob'

    def __str__(self):
        return str(self.data)
