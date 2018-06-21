from qubit_hamitonian import pyquil_program
from pyquil.api import QVMConnection

from pyquil.quil import Program

qvm = QVMConnection()
wf = qvm.wavefunction(pyquil_program)
print(wf)
