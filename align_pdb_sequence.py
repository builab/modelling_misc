#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 2024/06/04

"""
@Script: Script to align all the pdbs with corresponding sequences
@csv file format: pdb file name, UniprotID
@Warning: only deal with pdb with 1 chain only
@Usage: runscript align_pdb_csv.py example_pdb_uniprot.csv aln_dir
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
		uniprotID = row[1]
		aln_name = pdb_name.replace('.pdb', '.aln').replace('.cif', '.aln')
		run(session, f'close session')
		pdb = run(session, f'open {pdb_name}')[0]
		alignment = run(session, f'sequence align #{pdb.id_string},{uniprotID} program clustalOmega')
		#print(alignment.__dir__())
		run(session, f'save {output_dir}/{aln_name} format aln alignment {alignment.ident}')
