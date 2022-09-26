import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_aray(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k <= self._n:
            raise IndexError('Invalid Index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
            self._A[self._n] = obj
            self._n += 1

    def _resize(self, c):
        
 
def main():
    return True

main()
