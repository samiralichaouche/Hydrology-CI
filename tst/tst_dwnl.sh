#!/bin/bash

INPUTCSV=http://rapid-hub.org/data/angles_UCI_CS.csv
OUTPUTCSV=http://rapid-hub.org/data/angles_UCI_CS_out.csv

wget -O angles_UCI_CS.csv $INPUTCSV
wget -O angles_UCI_CS_out.csv $OUTPUTCSV
