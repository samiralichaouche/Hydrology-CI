#!/bin/bash

#Get Path for current working directory and input/output
cwd=$(pwd)
input_path="$cwd/angles_UCI_CS.csv"
output_path="$cwd/output.csv"

#Create Path for compute_cosines
parentdir="$(dirname "$cwd")"
computedir=$parentdir
computedir+="/src/compute_cosines.py"

#Download csv files
sh tst/tst_dwnl.sh

#Run compute cosines to generate output csv file
python ./src/compute_cosines.py $input_path $output_path

#Create Path for comp_csv
compdir=$cwd
compdir+="/tst_comp_csv.py"

#Compare the csv files and output result
python $compdir output.csv angles_UCI_CS_out.csv

#Remove extra files
rm *.csv
rm -f -- *.pyc
