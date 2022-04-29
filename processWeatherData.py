import pandas as pd


def get_weather_data():
    weather_data = pd.read_csv('./data/weather_data.csv', delimiter=',')
    cols = ['DATE', 'TAVG']
    weather_data = weather_data[cols].dropna().reset_index()
    weather_data = weather_data.rename(columns={'DATE': 'Date', 'TAVG': 'avg_temp'})
    weather_data['Date'] = pd.to_datetime(weather_data['Date']).dt.date
    return weather_data


if __name__ == '__main__':
    print(get_weather_data())