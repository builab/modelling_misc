# Modelling_misc

## xlinkcsv2chimeraX.py 
Generating Xlink intra and inter .pb files to load in ChimeraX

> Input: xlink.csv (see example, must follow strict format)

> Output: intra and inter .pb files and the ChimeraX loading file xlink.cxc

  python xlinkcsv2chimeraX.py --i xlink.csv --o xlink.cxc

# ChimeraX Python script
Running these inside ChimeraX

### chimerax_mm_and_save.py
Matchmaker many pdb models to a reference model and save the aligned files with a suffix.

> Input: reference pdb files, pdb_dir contains many pdb files

> Output: Output_dir contains aligned pdb files with suffix (default: '_aln.pdb')

  runscript chimerax_mm_and_save.py reference_pdb pdb_dir output_dir suffix
  

