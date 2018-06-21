After the classical calculcations have been done, the problem remains provide a map between electronic structure problems and qubit based quantum computers. The classically calculated Hamiltonian which is in second quantized representation needs to be mapped to qubit representation. This mapping is taken by certain transformations. Currently, most common ones are availaible in OpenFermion which are Jordan Wigner, Bravyi-Kitaev (BK) and Bravyi-Kitaev super fast (BKSF) transformations.  Each of these has different properties with regard to the Hamiltonians that are produced, which may offer benefits to different types of algorithms or experiments. OpenFermion attempts to remain agnostic to the particular transformation preferred by the user.

Methods have provided in OpenFermion to obtain the eigen values of the qubit hamiltonian. The lowest eigen value corresponds to the ground state energy. However these energy values have been calculated classically.

OpenFermion's core work is to produce the Qubit Operators pertaining to a certain problem. These operators are input for a number of quantum algorithms that then translate to quantum circuits. Currently, plugins are supported for the ProjectQ framework and the Rigetti Forest framework. 

Now we'll create a quantum circuit that is designed to prepare a unitary coupled cluster wavefunction on 4 qubits in the Jordan Wigner encoding. 

The quantum circuit we generate corresponds to the first-order Trotter evolution corresponding for t = 0.1s for a hydrogen molecule.

The quantum circuit looks as follows where the first few lines have been truncated.

H 0
H 1
RX(pi/2) 2
RX(pi/2) 3
CNOT 0 1
CNOT 1 2
CNOT 2 3
RZ(-0.009839529174273519) 3
CNOT 2 3
CNOT 1 2
CNOT 0 1
H 0
H 1
....................

Python libraries needed to run the files:
openfermionpyscf
pyscf
forestopenfermion
pyquil