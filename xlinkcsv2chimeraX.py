#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to convert a modified Xlink csv file to ChimeraX pseudobond file and display command
HB, McGill, 2022
"""

import pandas as pd
import argparse

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Xlink csv file to ChimeraX pseudobond & display command.\nWARNING: Strict Csv header column name\n')
	parser.add_argument('--i', help='Input CSV',required=True)
	parser.add_argument('--o', help='Output ChimeraX File',required=True)


	args = parser.parse_args()
  
	
	outChimera = open(args.o, 'w')
  outPseudo = open(str.replace(args.o, '.cxc', '.pb', 'w')
	df = pd.read_csv(args.i, header=[0], index_col=False)
  
  print(df)
	
	outPseudo.write(" ; halfbond = true\n")
  outPseudo.write(" ; color = magenta\n")
  outPseudo.write(" ; radius = 0.1\n")
  outPseudo.write(" ; dashes = 12\n")

	for i in range(len(df['X'])):
		outPseudo.write("\{:s}:{:d}@nz\' \{:s}:{:d}@nz\n".format(df, x, y, z, radius))
	/a:1@c3' /a:1@n3	
	outPseudo.close()
	
	
