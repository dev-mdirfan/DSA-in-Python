# Count the Number of Factors of a Number

class FactorCounter:
    def __init__(self, n):
        self.n = n

    def count_factors(self):
        count = 0
        for i in range(1, self.n+1):
            if self.n % i == 0:
                count += 1
                print(i, end=" ")
        print(f'\n{count}')

    def count_factors1(self):
        count = 0
        i = 1
        while i**2 <= self.n:
            if self.n % i == 0:
                count += 1
                if i**2 != self.n:
                    count += 1
            i += 1
        return count

    def count_factors2(self):
        if self.n < 0:
            return 0
        count = 0
        for i in range(1, int(self.n**0.5)+1):
            if self.n % i == 0:
                if self.n // i == i:
                    count += 1
                else:
                    count += 2
        return count

    def count_factors3(self):
        if self.n < 0:
            return 0
        return sum(
            1 if self.n // i == i else 2
            for i in range(1, int(self.n**0.5) + 1)
            if self.n % i == 0
        )

if __name__ == "__main__":
    n = 48
    factor_counter = FactorCounter(n)
    factor_counter.count_factors()
    print(factor_counter.count_factors1())
    print(factor_counter.count_factors2())
    print(factor_counter.count_factors3())
