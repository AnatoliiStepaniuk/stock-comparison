from scipy import stats

# Accepts array of yearly values and returns percentage of yearly growth
def growth(y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(y)), y)
    start = slope * 0 + intercept
    finish = slope * (len(y)-1) + intercept
    return (finish / start) ** (1 / len(y))
