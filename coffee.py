import numpy as np
import csv

def getData(data_path):
    coffee = []
    sleep = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return{'x': coffee,'y':sleep}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print('Corelation',corelation[0,1])

def setup():
    data_path = './coffee.csv'
    datasource = getData(data_path)
    findCorelation(datasource)


setup()    

     
