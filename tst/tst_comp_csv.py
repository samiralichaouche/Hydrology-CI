import urllib.request
import csv
import codecs

def comp_csv(inputcsv,outputcsv):
    """(compare two csv files given as arguments, w/ non-zero exit code if the files are not same)"""
    data_stream_i = urllib.request.urlopen(inputcsv)
    csv_reader = csv.reader(codecs.iterdecode(data_stream_i,'utf-8'))

    data_stream_o = urllib.request.urlopen(outputcsv)
    csv_reader_o = csv.reader(codecs.iterdecode(data_stream_o,'utf-8'))
    
    for input_row in csv_reader:
        output_row = next(csv_reader_o)
        if (input_row != output_row):
            return -1
    return 0
