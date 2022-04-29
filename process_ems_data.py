import datetime

import numpy as np
import pandas as pd

ems_data = pd.read_csv('./data/ems_data.csv', delimiter=',')
cols = ['Create_Date', 'EventFirstDispatched', 'EventFirstArrive']
ems_data = ems_data[cols].dropna().reset_index()

# Convert dates to timestamps
for col in cols:
    ems_data[col] = pd.to_datetime(ems_data[col], format='%m/%d/%Y %H:%M').astype(int)
    #ems_data[col] = (ems_data[col] - datetime.datetime(1970, 1, 1, 0, 0, 0))

ems_data = ems_data.drop(['index'], axis=1)

print(ems_data)