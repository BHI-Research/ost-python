#!/bin/bash

python3 ../../evaluator/evaluator.py -a data/ -u reference/ -v ../examples-utils/v60.mpg -m cus
echo ""
python3 ../../evaluator/evaluator.py -a data/ -u reference/ -v ../examples-utils/v60.mpg -m bhi
