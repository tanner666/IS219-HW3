class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation #function
    
    def get_result(self):
        #Getter method for stored operation
        return self.operation(self.a, self.b)