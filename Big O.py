# Growth Rates
# O(n) = Order of Magnitude
# T(n) = O(f(n))

class BigO:
    def __init__(self, n):
        self._count = n

    def setter(self):
        a = []
        a.append('O(log n)')
        a.append('O(n)')
        a.append('O(n log n)')
        a.append('O(n ** n)')
        a.append('O(n ** n ** n)')
        a.append('O(2 ** n)')
        a.append('O(n!)')
        
    
    def getter(self):
        x = 'Highest Exponent'
        y = 'Cut Constrant'
