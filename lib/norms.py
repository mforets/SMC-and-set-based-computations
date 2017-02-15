r"""

norms has methods to compute:

* matrix norm, induced by vector p-norms, for the simplest cases p = 1, 2, infty.

* the vector p norm for 1 <= p < infty with vecpnorm(b,p) and vecinftynorm(b) for p = infty

* the logarithmic norm of a matrix

AUTHORS :

- Marcelo Forets (2016-10)

NOTES :

- Sage already has norm method that can be applied to vectors and to matrix.
It is recommended to use that methods when possible. Allowable values are
'frob' (for the Frobenius norm), integers -2, -1, 1, 2 (default),  positive
and negative infinity. See docstring for further information. Computation is
performed  using the norm() function of SciPy/NumPy library.

- Resources for the the general case (p) for a matrix norm:
http://mathoverflow.net/questions/39148/efficiently-computing-a-matrixs-induced-p-norm

TO-DO :

- matrix p norm for arbitrary p.

"""

# This file was *autogenerated* from the file norms.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
#*****************************************************************************
#       Copyright (C) 2016 Marcelo Forets <mforets@nonlinearnotes.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import numpy as np

def matrix_1_norm(A):

    aux = _sage_const_0 
    for j in range(A.ncols()):
        aux2=_sage_const_0 
        for i in range(A.nrows()):
            aux2 += abs(A[i,j])
        if (aux2 > aux):
            aux = aux2

    return aux

def matrix_sup_norm(A):

    try:
        [nrows, ncols] = A.shape
    except:
        nrows = A.nrows(); ncols = A.ncols()

    aux = _sage_const_0 
    for i in range(nrows):
        aux2=_sage_const_0 
        for j in range(ncols):
            aux2 += abs(A[i,j])
        if (aux2 > aux):
            aux = aux2

    return aux

def matrix_2_norm(A):
    Q = A.H*A
    eval, evec = np.linalg.eig(Q.change_ring(RR))
    aux = sqrt(np.max(eval))

    return aux


def vector_1_norm(b):
    aux = _sage_const_0 
    for i in range(len(b)):
        aux += abs(b[i])

    return aux


def vector_sup_norm(b):
    aux = _sage_const_0 
    for i in range(len(b)):
        if (abs(b[i]) > aux):
            aux = abs(b[i])

    return aux


def vector_2_norm(b):
    aux = _sage_const_0 
    for i in range(len(b)):
        aux += b[i]**_sage_const_2 

    return sqrt(aux)

# p is a number: 1 <= p <= infty
def vector_p_norm(b,p):
    aux = _sage_const_0 

    if (p == 'inf'):
        for i in range(len(b)):
            if (abs(b[i]) > aux):
                aux = abs(b[i])

    else:    # if p < infty
        for i in range(len(b)):
            aux += abs(b[i])**p
        aux = aux**(_sage_const_1 /p)

    return aux

def log_norm(A, p='inf'):
    r"""Compute the logarithmic norm of a matrix.

    INPUTS:

    * "A" - A rectangular (Sage dense) matrix. The coefficients can be either real or complex.

    * "p" - (default: 'inf'). The vector norm; possible choices are 1, 2, or 'inf'.

    OUTPUT:

    * "lognorm" - The log-norm of A in the p norm.

    TO-DO:

    Add support for an arbitrary p >= 1 vector norm.

    """

    if (p == 'inf' or p == oo):
        n = A.nrows(); m = A.ncols();
        return max( real_part(A[i][i]) + sum( abs(A[i][j]) for j in range(m)) - abs(A[i][i]) for i in range(n))

    elif (p == _sage_const_1 ):
        n = A.nrows(); m = A.ncols();
        return max( real_part(A[j][j]) + sum( abs(A[i][j]) for i in range(n)) - abs(A[j][j]) for j in range(m))

    elif (p == _sage_const_2 ):

        if not (A.base_ring() == RR or A.base_ring() == CC):
            return _sage_const_1 /_sage_const_2 *max((A+A.H).eigenvalues())
        else:
            # Alternative, always numerical
            z = _sage_const_1 /_sage_const_2 *max( np.linalg.eigvals( np.matrix(A+A.H, dtype=complex) ) )
            return real_part(z) if imag_part(z) == _sage_const_0  else z

    else:
        raise ValueError('Value of p not understood or not implemented.')

