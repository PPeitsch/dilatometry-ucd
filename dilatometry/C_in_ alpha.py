# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:09:59 2016

@author: nasseh
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as P


def C_in_alpha(T):
    """
    This function calculates the mole fraction of Carbon (C) in alpha phase using thermocalc under para equilibrium.

    Parameters:
    T (float): The temperature at which the mole fraction is to be calculated.

    Returns:
    float: The absolute value of the calculated mole fraction of Carbon in alpha phase.
    """
    C = 1.4734491E-20 * T ** 6 + 3.9638142E-17 * T ** 5 - 1.1293268E-13 * T ** 4 + 6.8406210E-11 * T ** 3 - 9.3489472E-09 * T ** 2 + 6.1810195E-07 * T - 6.3920771E-06
    return abs(C)


MF_to_WP = np.array([4.88194823e-05, 2.14076779e+01, 1.69714954e+01, 1.16633462e+01, 1.70719962e+01])


def mf_to_wp(MF):
    return P.polyval(MF, MF_to_WP)


temp = np.linspace(800, 0, 100)
C = C_in_alpha(temp)
Cwp = mf_to_wp(C)
plt.plot(temp, Cwp)
