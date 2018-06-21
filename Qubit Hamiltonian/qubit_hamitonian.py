from openfermion.hamiltonians import MolecularData
from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermionpyscf import run_pyscf
from forestopenfermion import qubitop_to_pyquilpauli

from pyquil.quil import Program
from pyquil.paulis import exponentiate

basis = 'sto-3g'
multiplicity = 1
bond_length = 1.0
geometry = [('H', (0., 0., 0.)), ('H', (0., 0., bond_length))]
description = str(round(bond_length, 2))

molecule = MolecularData(
        geometry, basis, multiplicity, description=description)
molecule = run_pyscf(molecule, run_mp2=True, run_cisd=True, run_ccsd=True, run_fci=True)

# This is the Qubit hamiltonian that we obtain using the Jordan-Wigner transformation
h2_qubit_hamiltonian = jordan_wigner(get_fermion_operator(molecule.get_molecular_hamiltonian()))

# The qubit operator obtained is later converted to pyquil operatiors using an
# openfermion plugin called forestopenfermion
pyquil_hamiltonian = qubitop_to_pyquilpauli(h2_qubit_hamiltonian)

# With the data successfully transformed to pyquil transformation, the pyquil exponentiate routine is
# used to generate a quantum circuit corrensponding to the first-order Trotter evolution corresponding for t = 0.1s

pyquil_program = Program()
for term in pyquil_hamiltonian.terms:
    pyquil_hamiltonian += exponentiate(0.1*term)
print(pyquil_program)
