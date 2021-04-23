"""Profiling related code."""
from functools import wraps
import dis
import time

def timefn(fn):
    """Wrapper to profile the total time of a function's execution."""
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print("@timefn: {} took {} seconds".format(fn.func_name, t2 - t1))
        return result
    return measure_time

@timefn
def calculate_z_serial(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

def fast_function():
    return [i for i in range(1000)]

def slow_function():
    l = []
    for i in range(10000):
        l.append(i)
    return l

if __name__ == '__main__':
    # print(calculate_z_serial(1000, [1, 2, 3], [4, 5, 6]))