# Modelling Misc
Scripts to help modelling and visualization


## Pymol_cealign_AF.pml
Pymol script to use Cealign a pdb to a library of many AlphaFold models and calculating the RMSD. No sequence is used for this alignment.



## xlinkcsv2chimeraX.py 
Generating Xlink intra and inter .pb files to load in ChimeraX

> Input: xlink.csv (see example, must follow strict format)

> Output: intra and inter .pb files and the ChimeraX loading file xlink.cxc

  	python xlinkcsv2chimeraX.py --i xlink_example.csv --o xlink.cxc
  
  

# ChimeraX Python script
Running these inside ChimeraX

### chimerax_mm_and_save.py
Matchmaker many pdb models to a reference model and save the aligned files with a suffix.

> Input: reference pdb files, pdb_dir contains many pdb files

> Output: Output_dir contains aligned pdb files with suffix (default: '_aln.pdb')

  	runscript chimerax_mm_and_save.py reference.pdb pdb_dir output_dir suffix
  
  
### chimerax_fitmap_and_save.py
Fitmap many pdb models to a reference map and save the aligned files with a suffix.
The models need to be roughly aligned to the map, just small tweak needed.

> Input: map, pdb_dir contains many pdb files

> Output: Output_dir contains aligned pdb files with suffix (default: '_aln.pdb')

  	runscript chimerax_fitmap_and_save.py map.mrc pdb_dir output_dir suffix
  
  
### chimerax_align_pdb_sequence.py
Using a CSV file listing the same folder and corresponding UniprotID, perform alignment of PDB sequence and UniprotID to make sure no mutation is made during modelling.

> Input: map, pdb_dir contains many pdb files

> Output: Output_dir contains aligned pdb files with suffix (default: '_aln.pdb')

  	runscript chimerax_align_pdb_sequence.py pdb_uniprot.csv output_alignment_dir
  
  
  

 

  

