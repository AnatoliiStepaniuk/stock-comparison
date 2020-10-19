from scipy import stats
from scipy.optimize import curve_fit
import math


def exp_func(x, a, b):
    return b * (a ** x)


# Accepts array of yearly values and returns percentage of yearly growth
def linear_to_exp_growth(y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(y)), y)
    start = slope * 0 + intercept
    finish = slope * (len(y)-1) + intercept
    result = (finish / start) ** (1 / len(y))
    return result if not math.isnan(result) else "N/A"


def exp_growth(y):
    if len(y) < 2:
        return "N/A"
    popt, pcov = curve_fit(exp_func, range(1, len(y)+1), y)
    return popt[0]