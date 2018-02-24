#!/bin/bash

#Get Path for current working directory and input/output
cwd=$(pwd)
input_path="$cwd/angles_UCI_CS.csv"
output_path="$cwd/output.csv"

#Download csv files
#sh tst_dwnl.sh

#Run compute cosines to generate output csv file
python /c/Users/Samir/Desktop/HydrologyContinuousIntegrationProject/src/compute_cosines.py $input_path $output_path

#python -c "import tst_comp_csv; i = tst_comp_csv.comp_csv(\"output.csv\",\"output_tst.csv\"); print(i)"
