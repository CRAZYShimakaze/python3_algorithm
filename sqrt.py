a = 60


def sqtr(a):
    def sqt(a):
        if abs(a**2 - target) < 0.1:
            return a
        elif a**2 > target:
            return sqt(a / 2)
        else:
            return sqt(a / 2 * 3)

    target = a
    a /= 2
    c = sqt(a)
    return c


def s(x):
    low = 0
    high = x
    while abs(((low + high) / 2)**2 - x) > 0.01:
        if ((low + high) / 2)**2 > x:
            high = (low + high) / 2
        else:
            low = (low + high) / 2
    return (low + high) / 2


c = s(a)
print(c)