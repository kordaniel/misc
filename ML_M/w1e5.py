import math


def fun(x):
    return math.exp(x) + x**2 - 10*x + 2


def fun_der(x):
    return math.exp(x) + 2*x - 10


def locate_compute_min(fun, fun_der, precision = 1e-5, print_debug = False):
    x = 0               # x-value, where we are evaluating
    d = 2               # x-delta, how large steps we are taking
    cur = fun(x)        # fun(x) = cur, the value of the function at pos x
    f_min = math.inf    # minimum value we have seen
    angle = 1           # the derivative of the function at position x

    hist = [-1, -2]     # if these values are the same we have taken >1 steps
                        # in the same direction along the x-axis
    i = 0               # indexing hist

    while abs(cur - f_min) > precision or abs(angle) > precision**2:
        f_min = min(f_min, cur)
        angle = fun_der(x)
        if print_debug:
            print('x=', x)
            print('fx=', cur)
            print('dx=', fun_der(x))
            print('his', hist)
            if input() in ['x', 'q']: break


        if hist[0] == hist[1]:
            d *= 2
        else:
            d /= 2

        if angle > 0:
            hist[i] = 1
            x -= d
        else:
            hist[i] = 0
            x += d

        i = (i + 1) % 2
        cur = fun(x)

    return x, cur


def main():
    x, val = locate_compute_min(fun, fun_der)
    print(f'Found minimum f({x}) = {val}')

main()
