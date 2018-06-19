from openfermionprojectq import uccsd_trotter_engine, uccsd_singlet_evolution
from projectq.backends import CommandPrinter
from projectq.ops import X

from example2 import molecule

compiler_engine = uccsd_trotter_engine(compiler_backend=CommandPrinter())
wavefunction = compiler_engine.allocate_qureg(molecule.n_qubits)
test_amplitudes = [-1.03662149e-08, 5.65340580e-02]
evolution_operator = uccsd_singlet_evolution(test_amplitudes, molecule.n_qubits, molecule.n_electrons)
print('Sample output')
for i in range(molecule.n_electrons):
    X | wavefunction[i]
evolution_operator | wavefunction
compiler_engine.flush()
