# Look at strings, Parse header info by keys
# make it into a GUI.
# Make all data fields a dictionary
from pathlib import Path
from pprint import pprint
import json

file_name = "sample_email.txt"

results = dict()

with open(file_name, mode="r") as f:
    email_data=f.readlines()

custom_key = str()
custom_value = str()

current_line_is_key = bool()
last_line_is_key = False

for e_data_line in email_data:
    if e_data_line.startswith(" "):
        current_line_is_key = False
        custom_value += e_data_line.strip(" ").strip("\n").replace("        ","")
    else:
        current_line_is_key = True
        line = e_data_line.split(":",1)
        custom_key = line[0]
        rest_of_it = "\n".join(line[1:])
        custom_value += rest_of_it.strip(" ").strip("\n").replace("        ","")

    if last_line_is_key is False and current_line_is_key is True or last_line_is_key and current_line_is_key: 
        results |= {custom_key:custom_value}
        custom_key = ""
        custom_value = ""
    
    last_line_is_key = current_line_is_key

print(json.dumps(results, indent=4))
