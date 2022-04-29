from combineData import combine_data
from processEmsData import get_ems_data
from processWeatherData import get_weather_data


if __name__ == '__main__':
    ems_data = get_ems_data()
    weather_data = get_weather_data()
    combined_data = combine_data(ems_data, weather_data)

    combined_data.to_csv('./data/emsMetaData.csv')