import numpy as np
import pandas as pd
import perfplot


def setup(n):
    df = pd.DataFrame(np.random.randn(n))
    df[df > 0.9] = np.nan
    return df


def isnull_any(df):
    return df.isnull().any()


def isnull_values_sum(df):
    return df.isnull().values.sum() > 0


def isnull_sum(df):
    return df.isnull().sum() > 0


def isnull_values_any(df):
    return df.isnull().values.any()


perfplot.save(
    "out.png",
    setup=setup,
    kernels=[isnull_any, isnull_values_sum, isnull_sum, isnull_values_any],
    n_range=[2 ** k for k in range(25)],
)