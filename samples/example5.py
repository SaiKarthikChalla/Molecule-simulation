from example2 import molecule

from openfermion.transforms import jordan_wigner, get_fermion_operator
from forestopenfermion import qubitop_to_pyquilpauli

from pyquil.quil import Program
from pyquil.gates import X
from pyquil.paulis import exponentiate
from pyquil.api import QVMConnection

from grove.pyvqe.vqe import VQE
from scipy.optimize import minimize

h2_qubit_hamiltonian = jordan_wigner(get_fermion_operator(molecule.get_molecular_hamiltonian()))
pyquil_hamiltonian = qubitop_to_pyquilpauli(h2_qubit_hamiltonian)
print(pyquil_hamiltonian)
#
# electrons_program = Program()
# electrons_program.inst([X(0), X(1)])
pyquil_program = Program()
for term in pyquil_hamiltonian.terms:
    pyquil_program += exponentiate(0.1*term)
print(pyquil_program)
# qvm = QVMConnection()
# wf = qvm.wavefunction(pyquil_program)
# print(wf)
# vqe_inst = VQE(minimizer=minimize, minimizer_kwargs={'method': 'nelder-mead'})
# result = vqe_inst.expectation(pyquil_program, pyquil_hamiltonian, None, qvm)
# print(result)
