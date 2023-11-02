# Matching Pymol Script
# @hb 2021
cd /Users/kbui2/Desktop/48nm

load "/Users/kbui2/Downloads/helices_drawn2.pdb", target

python

from pymol import cmd
from glob import glob
import os

f = open('log_tip_CP.txt', 'w')
for file in glob("AlphaFold/*/*model_1.pdb"):
	name =  os.path.basename(file)
	name= name.replace('.pdb', '')
	#print(name)
	cmd.load(file)
	output = cmd.cealign("target", name)
	cmd.delete(name)
	outsum = name + ",RMSD," + str(output["RMSD"]) + ",Alignment length," + str(output["alignment_length"])
	print(outsum)
	f.write(outsum)
	f.write("\n")

f.close()
cmd.delete("all")


python end


# To save
# save test.pdb, I7ME23_3bcc8_unrelaxed_model_1,state=-1