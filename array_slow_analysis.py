import array
import numpy

def main():
    L = list(range(100000000))
    A = array.array('l', range(100000000))
    N = numpy.array
    %timeit sum(L)
    %timeit sum(A)
    %timeit sum(N)