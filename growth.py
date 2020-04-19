from scipy import stats
from scipy.optimize import curve_fit
import math


def exp_func(x, a, b, c):
    return c * (a ** x) + b


# Accepts array of yearly values and returns percentage of yearly growth
def linear_to_exp_growth(y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(y)), y)
    start = slope * 0 + intercept
    finish = slope * (len(y)-1) + intercept
    result = (finish / start) ** (1 / len(y))
    return result if not math.isnan(result) else "N/A"


def exp_growth(y):
    popt, pcov = curve_fit(exp_func, range(0, len(y)), y)
    return popt[0]
