import sys
sys.path.append("..")

class Calculate(object):
    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2, 2)
    print (result)
