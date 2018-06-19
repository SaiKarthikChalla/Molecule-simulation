from openfermion.transforms import jordan_wigner
from openfermion.ops import FermionOperator
from openfermion.utils import hermitian_conjugated
from forestopenfermion import qubitop_to_pyquilpauli, pyquilpauli_to_qubitop

from pyquil.quil import Program
from pyquil.gates import X
from pyquil.paulis import exponentiate
from pyquil.api import QVMConnection

hubbard_hamiltonian = FermionOperator()
spatial_orbitals = 4
for i in range(spatial_orbitals):
    electron_hop_alpha = FermionOperator(((2*i, 1), (2*((i+1) % spatial_orbitals), 0)))
    electron_hop_beta = FermionOperator(((2*i+1, 1), ((2 * ((i+1) % spatial_orbitals) + 1), 0)))
    hubbard_hamiltonian += -1 * (electron_hop_alpha + hermitian_conjugated(electron_hop_alpha))
    hubbard_hamiltonian += -1 * (electron_hop_beta + hermitian_conjugated(electron_hop_beta))
    hubbard_hamiltonian += FermionOperator(((2*i, 1), (2*i, 0), (2*i+1, 1), (2*i+1, 0)), 4.0)
hubbard_term_generator = jordan_wigner(hubbard_hamiltonian)
pyquil_hubbard_generator = qubitop_to_pyquilpauli(hubbard_term_generator)


localized_electrons_program = Program()
localized_electrons_program.inst([X(0), X(1)])
pyquil_program = Program()
for term in pyquil_hubbard_generator.terms:
    pyquil_program += exponentiate(0.1*term)
print (localized_electrons_program + pyquil_program)
qvm = QVMConnection()
print(qvm.run(pyquil_program, [0], 10))
wf = qvm.wavefunction(pyquil_program)
print(wf)
