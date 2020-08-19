import math
import numpy as np
from pyscf import gto, scf
from pyscf import cubegen, molden
from IPython.display import Image, display_png

HeH = gto.M(
    atom=[
        ['He',[0,0,0]],
        ['H',[0,0,1.4]]
    ],
    basis='sto-3g',
    unit='au',
    charge=1,
    verbose=3
)

mf = scf.RHF(HeH)
energy = mf.kernel()
#print(f'Cmatrix = {mf.mo_coeff}')
print(f'MO1 = {mf.mo_coeff[0,0]:8.2f}*He + {mf.mo_coeff[1,0]:8.2f}*H')
print(f'MO2 = {mf.mo_coeff[0,1]:8.2f}*He + {mf.mo_coeff[1,1]:8.2f}*H')

_=cubegen.orbital(HeH, 'HeH+_homo.cube',mf.mo_coeff[:,0])
_=cubegen.orbital(HeH, 'HeH+_lumo.cube',mf.mo_coeff[:,1])

#We use an external preview program to visualize the isosurfaces of
#the occupied orbital (green, isolevel = 0.1) and the unoccupied orbital
#(blue and red for isolevel = -0.1 and 0.1, respectively).
display_png(Image('HeH+_HomoLumo.png')) 