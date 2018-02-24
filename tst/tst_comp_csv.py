import csv

def comp_csv(inputcsv,outputcsv):
    """(compare two csv files given as arguments, w/ non-zero exit code if the files are not same)"""

    with open(inputcsv) as f:
        with open(outputcsv) as f2:
            
            csv_reader = csv.reader(f)
            csv_reader_o = csv.reader(f2)
            count = 0;
            for input_row in csv_reader:
                output_row = next(csv_reader_o)
                if (count != 0):
                    for i in range(len(input_row)):
                        input_row[i] = round(float(input_row[i]),3)
                    for i in range(len(output_row)):
                        output_row[i] = round(float(output_row[i]),3)
                if (input_row != output_row):
                    return -1
                count = 1
            return 0
    return 0
