import urllib.request
import csv
import codecs
import math

url = 'http://rapid-hub.org/data/angles_UCI_CS.csv'
data_stream = urllib.request.urlopen(url)
csv_reader = csv.reader(codecs.iterdecode(data_stream,'utf-8'))

next(csv_reader)
iddeg = []
for row in csv_reader:
    station_id = int(row[0])
    deg = int(row[1])
    iddeg.append((station_id,deg,math.cos(deg)))

for row in iddeg:
    print('station_id: {}, angle_degrees: {}, cosine value: {}'.format(row[0], row[1], row[2]))
