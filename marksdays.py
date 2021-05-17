import numpy as np
import csv

def getData(data_path):
    marks = []
    days = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    return{'x': marks,'y':days}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print('Corelation',corelation[0,1])

def setup():
    data_path = './marksdays.csv'
    datasource = getData(data_path)
    findCorelation(datasource)


setup()    

     
