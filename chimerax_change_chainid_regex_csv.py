#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 2024/06/04
# TO DO: Check for duplicate

"""
@Script: Script to change all the pdbs with corresponding chainid defined in a csv file
@csv file format: filename_pattern, chainID, common_tag
@Warning: only deal with pdb with 1 chain only
@A bit flexible in naming than chimerax_change_chainid_csv.py
@Usage: runscript chimerax_change_chainid_regex_csv.py example_regex_chainid.csv input_dir output_dir
@Authors Huy Bui
"""

import sys,os,time,csv
import os.path

def find_files_with_pattern(directory, pattern):
    # List to store matching file names
    matching_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if file name starts with the given pattern
            if file.startswith(pattern):
                matching_files.append(os.path.join(root, file))

    return matching_files


if len(sys.argv) < 4:
    print("Usage: runscript chimerax_change_chainid_regex_csv.py example_regex_chainid.csv input_dir output_dir")
    
csv_file = sys.argv[1]
input_dir = sys.argv[2]
output_dir = sys.argv[3]

print(f'Making {output_dir} directory')
os.makedirs(output_dir, exist_ok=True)

# This load to ChimeraX
from chimerax.core.commands import run

with open(csv_file, 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader: #
        if row[0].startswith('#'):
            continue
            
        prefix = row[0]
        chainid = row[1]
        tag = row[2]
        
        pdb_name = find_files_with_pattern(input_dir, prefix)
        if len(pdb_name) > 2:
            print("Error: Two files matched")
            continue
        elif len(pdb_name) == 0:
            print(f"Error: No file match {file_prefix}")
            continue
        else:
           output_name = f'{prefix}_{tag}_{chainid}.pdb'
            
        #run(session, f'close session')
        print(f"Opening {pdb_name[0]}")
        pdb = run(session, f'open {pdb_name[0]}')[0]
        run(session, f'changechains #{pdb.id_string} {chainid}')
        print(f"Writing {output_dir}/{output_name} with new chainID {chainid}")
        run(session, f'save {output_dir}/{output_name} models #{pdb.id_string}')
