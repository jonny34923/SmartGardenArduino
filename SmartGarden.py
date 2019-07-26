import datetime as dt

import matplotlib.dates as md
import matplotlib.pyplot as plt
import pyrebase

config = {
  "apiKey": 'AIzaSyAYLz7cAacHV63YkS3pNh3XxF49oQWnNrE',
  "authDomain": "smartgarden-5d081,firebaseapp.com",
  "databaseURL": "https://smartgarden-5d081.firebaseio.com",
  "storageBucket": "smartgarden-5d081.appspot.com",
  "serviceAccount": "C:\\Users\\jonny\\Downloads\\smartgarden-5d081-firebase-adminsdk-ginh1-c37ca368ee.json",

}


def get_data(database):
    return database.get().val()

def setup_database(config):
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    return database

def test(config):
    timestamp = []
    plotData = []
    tempData = []
    moistData = []
    database = setup_database(config)
    constant_stream(database)
    # data = get_data(database)
    # print(data)
    # for pt in data['data']:
    #     data_pt = data['data'][pt]
    #     timestamp.append(data_pt['timestamp'])
    #     plotData.append(data_pt['light'])
    #     tempData.append(data_pt['temp'])
    #     moistData.append(data_pt['moist'])
    #
    # #gen_graph(timestamp, tempData, 'date ', 'temperature in C ')
    # #gen_graph(timestamp, plotData, 'date ', 'light ')
    # gen_graph(timestamp, moistData, 'date ', 'moisture ')

def constant_stream(database):
    while True:
        data = get_data(database)
        print(data)
        timestamp = []
        plotData = []
        tempData = []
        moistData = []
        for pt in data['data']:
            data_pt = data['data'][pt]
            timestamp.append(data_pt['timestamp'])
            plotData.append(data_pt['light'])
            tempData.append(data_pt['temp'])
            moistData.append(data_pt['moist'])

        fig, axs = plt.subplots(3)

        gen_graph_full(timestamp, tempData, 'date ', 'temperature in C ', axs[0])
        gen_graph_full(timestamp, plotData, 'date ', 'light ', axs[1])
        gen_graph_full(timestamp, moistData, 'date ', 'moisture ', axs[2])
        fig.set_size_inches(12, 7)
        plt.show(block=False)
        plt.pause(2)
        plt.close()

def gen_graph_full(timestamps, values, xtitle, ytitle, subplt):
    dates = [dt.datetime.fromtimestamp(ts / 1000) for ts in timestamps]
    datenums = md.date2num(dates)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=25)
    ax = plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    subplt.set_ylabel(ytitle)
    subplt.set_xlabel(xtitle)
    subplt.plot(datenums, values, color='skyblue')


def gen_graph(timestamps, values, xtitle, ytitle):
    dates = [dt.datetime.fromtimestamp(ts / 1000) for ts in timestamps]
    datenums = md.date2num(dates)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=25)
    ax = plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.ylabel(ytitle)
    plt.xlabel (xtitle)
    n = len(datenums)
    for i in range(1, n):
        plt.plot(datenums[: i], values[: i], color='skyblue')
        plt.show(block= False)
        plt.pause(1)
        plt.close()


def add_point(x, y):
    plt.scatter(x, y, zorder=2)
    plt.pause(0.05)

#df=pd.DataFrame({'x': range(1,11), 'y': np.random.randn(10) })

test(config)
