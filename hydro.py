import urllib.request
import csv
import codecs

url = 'http://rapid-hub.org/data/angles_UCI_CS.csv'
data_stream = urllib.request.urlopen(url)
csv_reader = csv.reader(codecs.iterdecode(data_stream,'utf-8'))

for row in csv_reader:
    print(row)
