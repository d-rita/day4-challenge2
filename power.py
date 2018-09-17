def power(a,b):
    if not isinstance(a, int) and not isinstance(b, int):
        return ('Error! Please input integer values as base and exponent.')
    else:
        if b==0:
            return 1
        elif b==1:
            return a
        else:
            return (a*power(a,b-1))
