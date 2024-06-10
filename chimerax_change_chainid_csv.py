#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 2024/06/04

"""
@Script: Script to change all the pdbs with corresponding chainid defined in a csv file
@csv file format: pdb file name, chainID
@Warning: only deal with pdb with 1 chain only
@Usage: runscript chimerax_change_chainid_csv.py example_pdb_chainid.csv output_dir
@Authors Huy Bui
"""

import sys,os,time,csv
import os.path
from datetime import datetime

csv_file = sys.argv[1]
output_dir = sys.argv[2]

os.makedirs(output_dir, exist_ok=True)

# This load to ChimeraX
from chimerax.core.commands import run

with open(csv_file, 'r') as file:
	my_reader = csv.reader(file, delimiter=',')
	for row in my_reader: #
		pdb_name = row[0]
		chainid = row[1]
		output_name = pdb_name.replace('.pdb',f'_{chainid}.pdb')
		#run(session, f'close session')
		pdb = run(session, f'open {pdb_name}')[0]
		run(session, f'changechains #{pdb.id_string} {chainid}')
		run(session, f'save {output_dir}/{output_name} models #{pdb.id_string}')
