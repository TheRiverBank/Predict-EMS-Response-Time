import pandas as pd


def combine_data(df1, df2):
    combined_data = pd.merge(df1, df2, how='outer', on='Date').drop(['index'], axis=1).dropna()
    combined_data = combined_data.reset_index().drop(['index'], axis=1)

    return combined_data


if __name__ == '__main__':
    pass
