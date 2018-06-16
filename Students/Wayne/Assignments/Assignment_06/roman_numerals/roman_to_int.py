class RomanToInt(object):

    @staticmethod
    def value_of(c):
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
        else:
            raise ValueError('''"Provided character must be one of
                             : I V X L C D M."''')

    @classmethod
    def convert(cls, s):

        result = 0
        for i, c in enumerate(s):
            if (i + 1) < len(s) and cls.value_of(c) < cls.value_of(s[i + 1]):
                result -= cls.value_of(c)
            else:
                result += cls.value_of(c)

        return result
