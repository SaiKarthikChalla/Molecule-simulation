from qiskit_acqua_chemistry import ACQUAChemistry

acqua_chemistry_dict = {
    'driver': {'name': 'HDF5'},
    'HDF5': {'hdf5_input': 'H2_equilibrium_0.735_sto-3g.hdf5'},
    'operator': {'name':'hamiltonian',
                 'qubit_mapping': 'parity',
                 'two_qubit_reduction': True},
    'algorithm': {'name': 'ExactEigensolver'}
}

#acqua_chemistry_dict['HDF5']['hdf5_input'] = 'LiH/0.8_sto-3g.hdf5'
solver = ACQUAChemistry()
result = solver.run(acqua_chemistry_dict)
print('Ground state energy (classical): {:.12f}'.format(result['energy']))
# Second, we use variational quantum eigensolver (VQE)
acqua_chemistry_dict['algorithm']['name'] = 'VQE'
acqua_chemistry_dict['optimizer'] = {'name': 'SPSA', 'max_trials': 350}
acqua_chemistry_dict['variational_form'] = {'name': 'RYRZ', 'depth': 3, 'entanglement':'full'}
acqua_chemistry_dict['backend'] = {'name': 'local_statevector_simulator'}

solver = ACQUAChemistry()
result = solver.run(acqua_chemistry_dict)
print('Ground state energy (quantum)  : {:.12f}'.format(result['energy']))
print("====================================================")
# You can also print out other info in the field 'printable'
for line in result['printable']:
    print(line)
