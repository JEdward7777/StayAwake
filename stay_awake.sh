#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Activate the virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Run the Python script with any passed arguments
python "$SCRIPT_DIR/stay_awake.py" "$@"

#read -n1 -r -p "Press any key to continue..." key
