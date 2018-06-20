from openfermion.hamiltonians import MolecularData

# Set parameters to make a simple molecule.
diatomic_bond_length = .7414
geometry = [('H', (0., 0., 0.)), ('H', (0., 0., diatomic_bond_length))]
basis = 'sto-3g'
multiplicity = 1
charge = 0
description = str(diatomic_bond_length)

# Make molecule and print out a few interesting facts about it.
molecule = MolecularData(geometry, basis, multiplicity,
                         charge, description)
print('Molecule has automatically generated name {}'.format(
    molecule.name))
print('Information about this molecule would be saved at:\n{}\n'.format(
    molecule.filename))
print('This molecule has {} atoms and {} electrons.'.format(
    molecule.n_atoms, molecule.n_electrons))
for atom, atomic_number in zip(molecule.atoms, molecule.protons):
    print('Contains {} atom, which has {} protons.'.format(
        atom, atomic_number))


# Load molecular data from the hdf5 files in the data directory of OpenFermion
molecule.load()

print('\nAt bond length of {} angstrom, molecular hydrogen has:'.format(
        diatomic_bond_length))
print('Hartree-Fock energy of {} Hartree.'.format(molecule.hf_energy))
print('MP2 energy of {} Hartree.'.format(molecule.mp2_energy))
print('FCI energy of {} Hartree.'.format(molecule.fci_energy))
print('Nuclear repulsion energy between protons is {} Hartree.'.format(
    molecule.nuclear_repulsion))
for orbital in range(molecule.n_orbitals):
    print('Spatial orbital {} has energy of {} Hartree.'.format(
        orbital, molecule.orbital_energies[orbital]))
