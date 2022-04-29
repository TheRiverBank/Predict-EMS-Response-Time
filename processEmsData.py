import numpy as np
import pandas as pd


def get_ems_data():
    ems_data = pd.read_csv('./data/ems_data.csv', delimiter=',')
    cols = ['Create_Date', 'EventFirstDispatched', 'EventFirstArrive']
    ems_data = ems_data[cols].dropna().reset_index()
    ems_data['Date'] = pd.to_datetime(ems_data['Create_Date'], format='%m/%d/%Y %H:%M').dt.date
    # Convert dates to timestamps
    for col in cols:
        ems_data[col] = (pd.to_datetime(ems_data[col], format='%m/%d/%Y %H:%M').astype(np.int64) / (10**9)).astype(int)

    ems_data = ems_data.drop(['index'], axis=1)

    return ems_data


if __name__ == '__main__':
    print(get_ems_data())