#!/usr/bin/env python

import csv
import math
import sys

def compute_cosines(inputcsv, outputcsv):
    with open(inputcsv,'rb') as f:
        csv_reader = csv.reader(f)
        
        header = next(csv_reader)
        header.append("angle_cosine")
        iddeg = []
        iddeg.append(header)

        for row in csv_reader:
            station_id = int(row[0])
            deg = int(row[1])
            deg_in_rad = deg * math.pi / 180
            cos = math.cos(deg_in_rad)
            if (len(str(cos)) > 3):
                cos = round(cos,3)
            iddeg.append([station_id,deg,cos])

        outputFile = open(outputcsv,'wb')
        with outputFile:
            writer = csv.writer(outputFile)
            writer.writerows(iddeg)

def main():
    compute_cosines(sys.argv[1], sys.argv[2])

main()
