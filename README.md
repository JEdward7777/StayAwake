# StayAwake
A simple Python script to help you stay focused and avoid distractions.

## Overview
StayAwake is a Python script that periodically pops up a message asking if you're feeling distracted or awake. Based on your response, the script adjusts the frequency of the pop-ups to minimize interruptions when you're focused and maximize them when you're distracted.

## Requirements
* Python installed on your system
* Git installed to clone the repository
* A virtual environment (venv) with the easygui package installed

## Installation
1. Clone the repository: `git clone https://github.com/JEdward7777/StayAwake.git`
2. Create a virtual environment: `python -m venv venv` (on Linux) or `py -m venv venv` (on Windows)
3. Activate the virtual environment: `source venv/bin/activate` (on Linux) or `venv\Scripts\activate` (on Windows)
4. Install the easygui package: `pip install easygui`

## Running the Script
To run the script, use one of the provided wrappers:

* On Linux: `./stay_awake.sh`
* On Windows: `stay_awake.bat`

## How it Works
The script uses a simple algorithm to adjust the frequency of the pop-ups based on your responses. If you respond that you're feeling distracted, the script will pop up more frequently. If you respond that you're feeling focused, the script will pop up less frequently.

## License
This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.
