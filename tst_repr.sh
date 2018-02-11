#!/bin/bash

python -c "import compute_cosines; compute_cosines.compute_cosines(\"input.csv\")"
python -c "import tst_comp_csv; i = tst_comp_csv.comp_csv(\"output.csv\",\"output_tst.csv\"); print(i)"
