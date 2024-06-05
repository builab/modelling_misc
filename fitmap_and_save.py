#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 2024/06/04

"""
@Script: Script to fit locally many models into a map and save the aligned position
@Usage: runscript fitmap_and_save.py map pdb_dir output_dir suffix
@Authors Huy Bui
"""

import sys,os,time
import os.path
from datetime import datetime

input_map = sys.argv[1]
pdb_dir = sys.argv[2]
output_dir = sys.argv[3]

if len(sys.argv) > 4:
	suffix = sys.argv[4]
else:
	suffix = 'aln'

os.makedirs(output_dir, exist_ok=True)

# This load to ChimeraX
from chimerax.core.commands import run

map = run(session, f'open {input_map}')[0]
run(session, f'volume #{map.id_string} step 1')
print('Reading ' +  input_map + ' to #' + map.id_string)


# Load every pdb in pdb_dir, align with the ref and save the aligned output
for pdb in os.listdir(pdb_dir):
	if pdb.endswith((".pdb", ".cif")):
		model = run(session, f'open {pdb_dir}/{pdb}')[0]
		pdb_basename = os.path.basename(pdb)
		pdb_basename = pdb_basename.replace('.pdb', '').replace('.cif', '')
		print('Reading ' +  pdb + ' to #' + model.id_string)
		run(session, f'fit #{model.id_string} inmap #{map.id_string}')
		run(session, f'save {output_dir}/{pdb_basename}_{suffix}.pdb models #{model.id_string} relModel #{map.id_string}')
		

