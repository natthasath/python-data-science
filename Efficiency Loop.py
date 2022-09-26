from matplotlib import pyplot
# Space Complexity
# Time Complexity (Compile & Running)
# f(n) = Efficiency

class Loop():
    def __init__(self, n):
        self._count = n
        self._round = 0
        self._inner = 0
        self._outer = 0

class Linear(Loop):
    def __init__(self, n):
        super().__init__(n)

    # f(n) = n
    def linear(self):
        for x in range(0, self._count):
            self._round += 1
        return 'Round Loop: ' + str(self._round)

    # f(n) = n / 2
    def linear_devide(self):
        for x in range(0, self._count, 2):
            self._round += 1
        return 'Round Loop: ' + str(self._round)

class Logarithmic(Loop):
    def __init__(self, n):
        super().__init__(n)

    # f(n) = log n
    def logarithmic_multiple(self):
        x = 1
        while x <= self._count:
            self._round += 1
            x *= 2
        return 'Round Loop: ' + str(self._round)

    # f(n) = log2 n
    def logarithmic_devide(self):
        x = self._count
        while x >= 1:
            self._round += 1
            x /= 2
        return 'Round Loop: ' + str(self._round)

class Nested(Loop):
    def __init__(self, n):
        super().__init__(n)

    # f(n) = n log n
    def linear_logarithmic(self):
        for x in range(0, self._count):
            self._outer += 1
            y = 1
            while y <= self._count:
                self._inner += 1
                y *= 2
        return ('Outer Loop: ' + str(self._outer) +
                '\nInner Loop: ' + str(self._inner // self._outer))

    # f(n) = n ** n
    def quadratic(self):
        for x in range(0, self._count):
            self._outer += 1
            for y in range(0, self._count):
                self._inner += 1
        return ('Outer Loop: ' + str(self._outer) +
                '\nInner Loop: ' + str(self._inner // self._outer))

    # f(n) = n ** [ (n + 1) / 2 ]
    def dependent_quadratic(self):
        for x in range(0, self._count):
            self._outer += 1
            for y in range(0, x + 1):
                self._inner += 1
        return ('Outer Loop: ' + str(self._outer) +
                '\nInner Loop: ' + str(self._inner / self._outer))

def main():
    c = int(input('Input Number: '))
    l = Linear(c)
    n = Nested(c)
    print(n.dependent_quadratic())
    
    """pyplot.subplot(2,1,1)
    pyplot.plot(a, color='blue', lw=2)
    pyplot.yscale('log')
    pyplot.show()"""

main()
        
