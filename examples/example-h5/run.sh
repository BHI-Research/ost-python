#!/bin/bash

python3 ../../evaluator/evaluator.py -a ../examples-utils/result.h5 -u ../examples-utils/OVP-dataset-UTN.h5 -v ../examples-utils/v60.mpg --user_summary_path v60/user_summary --automatic_summary_path v60/machine_summary -m cus
echo ""
python3 ../../evaluator/evaluator.py -a ../examples-utils/result.h5 -u ../examples-utils/OVP-dataset-UTN.h5 -v ../examples-utils/v60.mpg --user_summary_path v60/user_summary --automatic_summary_path v60/machine_summary -m bhi
