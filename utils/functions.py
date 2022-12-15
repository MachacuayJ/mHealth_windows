import numpy as np


def mean(x):
    return x.mean()


def max(x):
    return x.max()


def rango(x):
    return x.max()-x.min()


def std(x):
    return x.std()


def min(x):
    return x.min()


def var(x):
    return x.var()


def median(x):
    return np.median(x)


def sem(x):
    return x.std()/np.sqrt(x.shape[0])
