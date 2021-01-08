from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt


def pull_intraday_time_series_alpha_vantage(alpha_vantage_api_key, ticker_name, data_interval = '30min'):
    """
    Pull intraday time series data by stock ticker name.
    Args:
        alpha_vantage_api_key: Str. Alpha Vantage API key.
        ticker_name: Str. Ticker name that we want to pull.
        time_interval: Str. values like '1min', '5min', '15min', '30min', '60min'.
    Outputs:
        data: Dataframe. Time series data, including open, high, low, close, and datetime values.
        metadata: Dataframe. Metadata associated with the time series.
    """
    #Generate Alpha Vantage time series object
    ts = TimeSeries(key = alpha_vantage_api_key, output_format = 'pandas')
    #Retrieve the data for the past sixty days (outputsize = full)
    data, meta_data = ts.get_intraday(ticker_name, outputsize = 'full', interval= data_interval)
    data['date_time'] = data.index
    return data, meta_data

def plot_data(df, x_variable, y_variable, title):
    """
    Plot the x- and y- variables against each other, where the variables are columns in
    a pandas dataframe
    Args:
        df: Pandas dataframe, containing x_variable and y_variable columns.
        x_variable: String. Name of x-variable column
        y_variable: String. Name of y-variable column
        title: String. Desired title name in the plot.
    Outputs:
        Plot in the console.
    """
    fig, ax = plt.subplots()
    ax.plot_date(df[x_variable],
                 df[y_variable], marker='', linestyle='-', label=y_variable)
    fig.autofmt_xdate()
    plt.title(title)
    plt.show()
def main():
    #provide your key
    alpha_vantage_api_key="KJZN8FU1P3KW9ZIG"
    ts_data, ts_metadata = pull_intraday_time_series_alpha_vantage(alpha_vantage_api_key, ticker_name = "MRNA")
    #Plot the high prices
    plot_data(df = ts_data,
              x_variable = "date_time",
              y_variable = "2. high",
              title ="High Values, MRNA Stock, 30 Minute Data")

