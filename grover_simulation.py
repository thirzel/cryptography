from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the oracle for the search problem
def oracle(circuit, qubits):
    circuit.h(qubits)
    circuit.mct(qubits[:-1], qubits[-1])  # Multi-controlled Toffoli gate
    circuit.h(qubits)

# Define the Grover's diffusion operator
def diffusion_operator(circuit, qubits):
    circuit.h(qubits)
    circuit.x(qubits)
    circuit.h(qubits[-1])
    circuit.mct(qubits[:-1], qubits[-1])  # Multi-controlled Toffoli gate
    circuit.h(qubits[-1])
    circuit.x(qubits)
    circuit.h(qubits)

# Initialize the quantum circuit
num_qubits = 3  # Number of qubits in the circuit
grover_circuit = QuantumCircuit(num_qubits)

# Apply Hadamard gates to create superposition
grover_circuit.h(range(num_qubits))

# Apply the oracle
oracle(grover_circuit, range(num_qubits))

# Apply the Grover diffusion operator
diffusion_operator(grover_circuit, range(num_qubits))

# Measure the qubits
grover_circuit.measure_all()

# Execute the circuit on a simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(grover_circuit, simulator)
result = execute(compiled_circuit, simulator, shots=1024).result()
counts = result.get_counts()

# Visualize the results
plot_histogram(counts)
plt.show()
