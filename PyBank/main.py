import pandas as pd
from pathlib import Path

csv_path = Path('/Users/thanhle/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

budget_df = pd.read_csv(csv_path)

budget_df.head()
