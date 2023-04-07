# testing-techiques

## Setup Proyect

1. Create and source virtual environment

"""bash
virtualenv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
"""

2. Create Scaffold
"""bash
touch Makefile
touch requirements.txt
touch hello.py
touch test_hello.py

3. Populate "Makefile"
"""bash
install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

test:
    python -m pytest -vv --cov=hello test_hello.py


lint:
    pylint --disable=R,C hello hello.py


all: install lint test
"""

## How to debug

* print
* pdb
* testing