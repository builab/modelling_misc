#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to map the X-link residual to tubulin A & B from a CSV file to ChimeraX
Very specific script. Assumption that column 2 contains only TUBA or TUBB
Assume tubulin A and B has chain A & B
HB, McGill, 2022
"""

import pandas as pd
import argparse

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Xlink csv file to map CSV file to ChimeraX.\nWARNING: Strict Csv header column name\nUse --uniprot2 all for every protein\n')
	parser.add_argument('--i', help='Input CSV',required=True)
	parser.add_argument('--uniprot2', help='Uniprot of protein 2',required=True)
	parser.add_argument('--o', help='Output ChimeraX File',required=True)

	# In the future, perhaps try to have --uniprot1 to find both proteins

	args = parser.parse_args()
  
	
	outChimeraX = open(args.o, 'w')	
	df = pd.read_csv(args.i, header=[0])
  
	#print(df)
	if args.uniprot2 == "all":
		dfuniprot2 = df
	else:
		dfuniprot2 = df[df.Uniprot2 == args.uniprot2].copy()
	
	#print(dfuniprot2)
	
	for i in range(len(dfuniprot2)):
		#outChimeraX.write("show /{:s}:{:d}/{:s}:{:d} target a\n".format(df.loc[i, 'Chain1'], int(df.loc[i, 'PepPos1']) + int(df.loc[i, 'LinkPos1']) - 1, df.loc[i, 'Chain2'], int(df.loc[i, 'PepPos2']) + int(df.loc[i, 'LinkPos2']) - 1))
		residue = int(df.loc[i, 'PepPos1']) + int(df.loc[i, 'LinkPos1']) - 1
		if df.loc[i, 'Protein1'] == 'TUBA': # Link to alpha-tubulin
			outChimeraX.write("show /A:{:d} target a\ncolor /A:{:d} red target a\n".format(residue, residue))
		else: #Link to beta-tubulin
			outChimeraX.write("show /B:{:d} target a\ncolor /B:{:d} red target a\n".format(residue, residue))

	outChimeraX.write("style sphere\n")
	outChimeraX.close()