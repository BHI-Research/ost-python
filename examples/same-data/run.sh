#!/bin/bash

python3 ../../ost-python/ost/evaluator_cli.py -a data/ -u reference/ -v ../examples-utils/v60.mpg -m cus
echo ""
python3 ../../ost-python/ost/evaluator_cli.py -a data/ -u reference/ -v ../examples-utils/v60.mpg -m bhi
