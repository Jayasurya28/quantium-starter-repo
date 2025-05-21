#!/bin/bash

# Activate virtual environment
source ./venv/bin/activate  # Adjust path to your virtual env

# Run tests
pytest test_app.py -v
TEST_RESULT=$?

# Deactivate virtual environment
deactivate

# Exit with pytest exit code: 0 = success, otherwise 1
if [ $TEST_RESULT -eq 0 ]; then
  exit 0
else
  exit 1
fi
