from math import factorial


class binom:
    
    @staticmethod
    def C(k, n):
        return factorial(n) // (factorial(k) * factorial(n-k))

    def __init__(self, n):

        assert n >= 0 and isinstance(n, int)

        self.binoms = []
        for i in range(n+1):
            result = []
            for j in range(i+1):
                result.append(binom.C(j, i))
            self.binoms.append(result)

    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.binoms])

    def __iter__(self):
        return iter(self.binoms)
            
n = int(input('N: '))

print(binom(n))