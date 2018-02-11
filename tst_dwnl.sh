#!/bin/bash

INPUTCSV=http://rapid-hub.org/data/angles_UCI_CS.csv
OUTPUTCSV=http://rapid-hub.org/data/angles_UCI_CS_out.csv

wget -O input.csv $INPUTCSV
wget -O output.csv $OUTPUTCSV
