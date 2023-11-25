import pandas as pd
import numpy as np
import itertools
from itertools import combinations
from scipy.stats import chi2_contingency
npi = pd.read_csv("npi_sample.csv")

print(npi.head())

def chi_square_df(df):
  chi2_dict = {}
  combinations = list(itertools.combinations(npi.columns, 2))
  for combination in combinations:
    key = combination[0], combination[1]
    columns = df[combination[0]], df[combination[1]]

    frequency = pd.crosstab(df[combination[0]], df[combination[1]])
    chi2, pval, dof, expected = chi2_contingency(frequency)

    chi2_dict[key] = chi2

  df = pd.DataFrame(chi2_dict, index = [0])
  return df


df = chi_square_df(npi)
print(df.max())

