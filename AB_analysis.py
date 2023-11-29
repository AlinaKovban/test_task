import pandas as pd
from scipy.stats import ttest_ind

ab_result = pd.read_excel('AB test.xlsx', header=0)

ab_result['Group 1'] = pd.to_numeric(ab_result['Group 1'], errors='coerce')
ab_result['Group 2'] = pd.to_numeric(ab_result['Group 2'], errors='coerce')

ab_result = ab_result.dropna(subset=['Group 1', 'Group 2'])

t, p = ttest_ind(ab_result['Group 1'], ab_result['Group 2'])

print(f"t-test = {t:.3f}")
print(f"p-value = {p:.3f}")
