#!/bin/bash

INPUTCSV=http://rapid-hub.org/data/angles_UCI_CS.csv
OUTPUTCSV=http://rapid-hub.org/data/angles_UCI_CS_out.csv

curl -fsS -o angles_UCI_CS.csv $INPUTCSV
curl -fsS -o angles_UCI_CS_out.csv $OUTPUTCSV
