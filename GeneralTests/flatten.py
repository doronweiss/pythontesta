import functools
import itertools
import numpy
import operator
import perfplot


def forfor(a):
    return [item for sublist in a for item in sublist]


def sum_brackets(a):
    return sum(a, [])


def functools_reduce(a):
    return functools.reduce(operator.concat, a)


def functools_reduce_iconcat(a):
    return functools.reduce(operator.iconcat, a, [])


def itertools_chain(a):
    return list(itertools.chain.from_iterable(a))


def numpy_flat(a):
    return list(numpy.array(a).flat)


def numpy_concatenate(a):
    return list(numpy.concatenate(a))


perfplot.show(
    setup=lambda n: [list(range(10))] * n,
    kernels=[
        forfor, sum_brackets, functools_reduce, functools_reduce_iconcat,
        itertools_chain, numpy_flat, numpy_concatenate
        ],
    n_range=[2**k for k in range(16)],
    logx=True,
    logy=True,
    xlabel='num lists'
    )