import operator


class _Number:
    def __init__(self, num, b=10):
        if b < 2:
            raise ValueError("Cannot convert {} to base {}.".format(num, b))
        self._num = str(int(num))
        self.base = b

    def __str__(self):
        return self._num
    
    def __int__(self):
        if self.base == 10:
            return int(self._num)
        return int(self.to_base_ten())
    
    def __repr__(self):
        return f"<int({self.to_base_ten()}) in Base {self.base}>"

    def to_base_ten(self):
        digits = list(self._num)
        neg = '-' in digits
        if neg: digits.remove('-')
        digits.reverse()
        x = 0
        for i, index in zip(digits, range(len(self._num))):
            x += int(i) * (self.base ** index)
        return _Number('-' + str(x) if neg else x)

    def to_base(self, b):
        n, digits = int(self), []
        while n >= b:
            i = n - n % b
            digits.append(str(int(i/b)))
            n -= i
        digits.append(str(n))
        return _Number(''.join(digits), b)

    def __sub__(self, other):
        return self.op(operator.sub, other)
    
    def __add__(self, other):
        return self.op(operator.add, other)
    
    def __mul__(self, other):
        return self.op(operator.mul, other)
    
    def __truediv__(self, other):
        return self.op(operator.truediv, other)
    
    def __mod__(self, other):
        return self.op(operator.mod, other)
    
    def __abs__(self):
        return self.op(operator.abs)

    def op(self, func, *other):
        # Check type other
        dif = func(int(self), *[int(x) for x in other])
        n = _Number(dif)
        return n.to_base(self.base)
