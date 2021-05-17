import numpy as np
import csv

def getData(data_path):
    ic = []
    temp = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ic.append(float(row['Ice-cream Sales']))
            temp.append(float(row['Temperature']))
    return{'x': ic,'y':temp}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print('Corelation',corelation[0,1])

def setup():
    data_path = './IceTemp.csv'
    datasource = getData(data_path)
    findCorelation(datasource)


setup()    

     
