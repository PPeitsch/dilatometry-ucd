import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as P


def calculate_carbon_mole_fraction_in_alpha(temp):
    """
    This function calculates the mole fraction of Carbon (C) in alpha phase using thermocalc under para equilibrium.

    Parameters:
    temp (float): The temperature at which the mole fraction is to be calculated.

    Returns:
    float: The absolute value of the calculated mole fraction of Carbon in alpha phase.
    """
    carbon_mole_fraction = 1.4734491E-20 * temp ** 6 + 3.9638142E-17 * temp ** 5 - 1.1293268E-13 * temp ** 4 + 6.8406210E-11 * temp ** 3 - 9.3489472E-09 * temp ** 2 + 6.1810195E-07 * temp - 6.3920771E-06
    return abs(carbon_mole_fraction)


mole_fraction_to_weight_percent = np.array(
    [4.88194823e-05, 2.14076779e+01, 1.69714954e+01, 1.16633462e+01, 1.70719962e+01])


def convert_mole_fraction_to_weight_percent(mole_fraction):
    return P.polyval(mole_fraction, mole_fraction_to_weight_percent)


temperature_range = np.linspace(800, 0, 100)
carbon_mole_fraction = calculate_carbon_mole_fraction_in_alpha(temperature_range)
carbon_weight_percent = convert_mole_fraction_to_weight_percent(carbon_mole_fraction)
plt.plot(temperature_range, carbon_weight_percent)
