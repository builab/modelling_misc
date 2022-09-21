#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to convert a modified Xlink csv file to ChimeraX pseudobond file and display command
Generate a intraXlink peseudobond, interXlink Pseudobond and a chimera loading and display script
HB, McGill, 2022
"""

import pandas as pd
import argparse

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Xlink csv file to ChimeraX pseudobond & display command.\nWARNING: Strict Csv header column name\n')
	parser.add_argument('--i', help='Input CSV',required=True)
	parser.add_argument('--o', help='Output ChimeraX File',required=True)


	args = parser.parse_args()
  
	
	outChimeraX = open(args.o, 'w')	
	outPseudoIntra = open(str.replace(args.o, '.cxc', '_intra.pb'), 'w')
	outPseudoInter = open(str.replace(args.o, '.cxc', '_inter.pb'), 'w')

	df = pd.read_csv(args.i, header=[0])
  
	#print(df)
	
	outPseudoIntra.write(" ; halfbond = true\n")
	outPseudoIntra.write(" ; color = magenta\n")
	outPseudoIntra.write(" ; radius = 0.1\n")
	outPseudoIntra.write(" ; dashes = 12\n")
	
	outPseudoInter.write(" ; halfbond = true\n")
	outPseudoInter.write(" ; color = yellow\n")
	outPseudoInter.write(" ; radius = 0.1\n")
	outPseudoInter.write(" ; dashes = 12\n")
	

	# In the future, make inter & intra link separate file
	for i in range(len(df['Chain1'])):
		if df.loc[i, 'Chain1'] == df.loc[i, 'Chain2']: # IntraLink
			outPseudoIntra.write("\{:s}:{:d}@nz\' \{:s}:{:d}@nz\n".format(df.loc[i, 'Chain1'], int(df.loc[i, 'PepPos1']) + int(df.loc[i, 'LinkPos1']) - 1, df.loc[i, 'Chain2'], int(df.loc[i, 'PepPos2']) + int(df.loc[i, 'LinkPos2']) - 1))
		else: #InterLink
			outPseudoInter.write("\{:s}:{:d}@nz\' \{:s}:{:d}@nz\n".format(df.loc[i, 'Chain1'], int(df.loc[i, 'PepPos1']) + int(df.loc[i, 'LinkPos1']) - 1, df.loc[i, 'Chain2'], int(df.loc[i, 'PepPos2']) + int(df.loc[i, 'LinkPos2']) - 1))

	
	outPseudoIntra.close()
	outPseudoInter.close()
	
	outChimeraX.write('crosslink abc def\n')
	outChimeraX.close()