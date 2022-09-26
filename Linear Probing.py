class Hash():
    def __init__(self):
        self._table = [0] * 13
        self._size = 13

    def hash_function(self, x):
        return x % 13

    def add_key(self, x):
        key = Hash.hash_function(self, x)
        if self._table[key] == 0:
            self._table[key] = x
        else:
            while True:
                key += 1
                if self._table[key] == 0 and key < self._size:
                    self._table[key] = x
                    break
                else:
                    key = Hash.hash_function(self, key)
                    
    def get_key(self, key):
        return self._table[key]

    def __str__(self):
        return str(self._table)

def main():
    h = Hash()
    h.add_key(18)
    h.add_key(41)
    h.add_key(22)
    h.add_key(44)
    h.add_key(59)
    h.add_key(32)
    h.add_key(31)
    h.add_key(73)
    print(h)

main()
