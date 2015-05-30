import os
import sys
import numpy as np

ref_cat = 'FINAL.onlykindadinal.cl0023.deimos.lris.feb2010.cat'
outreg = 'Cl0023.opt_ds9.%s.reg'
matched_errR = 2.5

ref_load_dict={'names':('ID','ra','dec','magI'),'formats':('string','f8','f8','f8')}
cr_opt = np.loadtxt(ref_cat,dtype=ref_load_dict,usecols=(1,3,4,9))
ra_opt,dec_opt,magI_opt,id_opt = cr_opt['ra'],cr_opt['dec'],cr_opt['magI'],cr_opt['ID']

FILE=open(outreg,'w')
FILE.write("# Region file format: DS9 version 4.1\n")
FILE.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
for i in range(0L,len(cr_opt)):
  FILE.write("circle(" + str(ra_opt[i]) + "," + str(dec_opts[i]) + "," + str(matched_errR) + '")\n')
