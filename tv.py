import numpy as np
import csv

def getData(data_path):
    size = []
    time = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size.append(float(row['Size of TV']))
            time.append(float(row['Average time']))
    return{'x': size,'y':time}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print('Corelation',corelation[0,1])

def setup():
    data_path = './tv.csv'
    datasource = getData(data_path)
    findCorelation(datasource)


setup()    

     
