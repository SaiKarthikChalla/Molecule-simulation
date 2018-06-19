from openfermion.hamiltonians import MolecularData
from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermionpyscf import run_pyscf

basis = 'sto-3g'
multiplicity = 1
bond_length = 1.0
geometry = [('H', (0., 0., 0.)), ('H', (0., 0., bond_length))]
description = str(round(bond_length, 2))

molecule = MolecularData(
        geometry, basis, multiplicity, description=description)
molecule = run_pyscf(molecule, run_mp2=True, run_cisd=True, run_ccsd=True, run_fci=True)

h2_qubit_hamiltonian = jordan_wigner(get_fermion_operator(molecule.get_molecular_hamiltonian()))
