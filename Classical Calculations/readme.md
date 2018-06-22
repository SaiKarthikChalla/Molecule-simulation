**OpenFermion** requires certain energy calculations to be done before proceeding to the quantum computations so that these calculations form an initial guess. The calculations are done through various chemistry electronic structure packages such as **PyScf** and **Psi4**. Right now, there are plugins available for these both packages only.
This directory consists of classical energy calculations of the hydrogen molecule using the PyScf package. It performs certain Hartree-Fock calculations to do these calculations. The PyScf calculates the Molecular Hamiltonian and various density matrices.
We'll initialize a hydrogen molecule and calculate various energies such as Hartree-Fock energy, MP2 energy, FCI energy and orbital energies for the molecule at various bond lengths and plot the energies.
The minimum energy of the molecule corresponds to the bondlength of the molecule and the structure of the molecule.

The following line performs the classical calculations
``` python
molecule = run_pyscf(molecule, run_mp2=True, run_cisd=True, run_ccsd=True, run_fci=True)
```
The calculations are stored in the molecule object

Python libraries to be installed:
* openfermionpyscf
* pyscf 
