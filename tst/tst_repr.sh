#!/bin/bash

#Get Path for current working directory and input/output
cwd=$(pwd)
input_path="$cwd/angles_UCI_CS.csv"
output_path="$cwd/output.csv"

parentdir="$(dirname "$cwd")"
computedir=$parentdir
computedir+="/src/compute_cosines.py"

#Download csv files
sh tst_dwnl.sh

#Run compute cosines to generate output csv file
python $computedir $input_path $output_path


