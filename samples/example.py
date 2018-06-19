from openfermion.hamiltonians import MolecularData
from openfermionpyscf import run_pyscf

basis = 'sto-3g'
multiplicity = 1
bond_length_interval = 0.1
n_points = 10

hf_energies = []
fci_energies = []
bond_lengths = []
for point in range(15, 20):
    bond_length = bond_length_interval * point
    bond_lengths += [bond_length]
    description = str(round(bond_length, 2))
    print(description)
    geometry = [('Cl', (0., 0., 0.)), ('Cl', (0., 0., bond_length))]
    molecule = MolecularData(
        geometry, basis, multiplicity, description=description)
    
    # Run the calculations.
    molecule = run_pyscf(molecule, run_mp2=True, run_cisd=True, run_ccsd=True, run_fci=True)

    # Print out some results of calculation.
    print('\nAt bond length of {} angstrom, molecular chlorine has:'.format(
        bond_length))
    print('Hartree-Fock energy of {} Hartree.'.format(molecule.hf_energy))
    print('MP2 energy of {} Hartree.'.format(molecule.mp2_energy))
    print('FCI energy of {} Hartree.'.format(molecule.fci_energy))
    print('Nuclear repulsion energy between protons is {} Hartree.'.format(
        molecule.nuclear_repulsion))
    for orbital in range(molecule.n_orbitals):
        print('Spatial orbital {} has energy of {} Hartree.'.format(
            orbital, molecule.orbital_energies[orbital]))
    hf_energies += [molecule.hf_energy]
    fci_energies += [molecule.fci_energy]

# Plot.
import matplotlib.pyplot as plt

plt.figure(0)
plt.plot(bond_lengths, fci_energies, 'x-')
plt.plot(bond_lengths, hf_energies, 'o-')
plt.ylabel('Energy in Hartree')
plt.xlabel('Bond length in angstrom')
plt.show()
