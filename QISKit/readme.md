We'll see how to solve the Hamiltonian problem in IBM's QISKit library. We'll initialize a hydrogen molecule and solve the hydrogen
Hamiltonian both in a classic way and quantum way. Classically, this is done using Exact eigen solver. In a quantum way, Variational eigen solver is a 
quantum algorithm to solve the electronic structure problem. This algorithm is executed in our local machine. The output consists of ground state energies, nuclear repulsion energies
and dipole moment of the molecule.
The output we get for hydrogen molecule is as follows:

Ground state energy (classical): -1.137306035753
Ground state energy (quantum)  : -1.137303951018
====================================================
=== GROUND STATE ENERGY ===
 
* Electronic ground state energy (Hartree): -1.857272942297
  - computed part:      -1.857272942297
  - frozen energy part: 0.0
  - particle hole part: 0.0
~ Nuclear repulsion energy (Hartree): 0.719968991279
> Total ground state energy (Hartree): -1.137303951018
  Measured:: Num particles: 2.000, S: 0.000, M: 0.00000
 
=== DIPOLE MOMENT ===
 
* Electronic dipole moment (a.u.): [0.0  0.0  0.00074671]
  - computed part:      [0.0  0.0  0.00074671]
  - frozen energy part: [0.0  0.0  0.0]
  - particle hole part: [0.0  0.0  0.0]
~ Nuclear dipole moment (a.u.): [0.0  0.0  0.0]
> Dipole moment (a.u.): [0.0  0.0  0.00074671]  Total: 0.00074671
               (debye): [0.0  0.0  0.00189796]  Total: 0.00189796