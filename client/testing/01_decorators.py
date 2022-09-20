
def dec1(f):
    def wrapper(*args, dec=None, **kwargs):
        print('Start D1')
        if not dec:
            dec = True
        f_res = f(*args, dec=dec, **kwargs)
        print('End D1')
        return f_res
    return wrapper

def dec2(f):
    def wrapper(*args, dec=None, **kwargs):
        print('Start D2')
        if not dec:
            dec = True
        elif dec == True:
            dec = 44
        f_res = f(*args, dec=dec, **kwargs)
        print('End D2')
        return f_res
    return wrapper


@dec1
@dec2
def fun(dec=None):
    print('FUN:', dec)

fun()
