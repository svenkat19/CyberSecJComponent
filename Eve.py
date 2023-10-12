from qubit import Qubit
import random
class Eve:
    def __init__(self):
        pass

    def intercept_and_forward(self, qubits):
        return qubits  # Eve does nothing with the qubits, just forwards them

    def measure_qubits(self, qubits):
        orientations = [0 if random.random() < 0.5 else 1 for _ in qubits]
        measurements = []

        for i in range(len(qubits)):
            if orientations[i] == 0:
                measurements.append(qubits[i].measure("horizontal"))
            else:
                measurements.append(qubits[i].measure("vertical"))

        return measurements


'''import random
from qubit import Qubit
class Eve(object):
    def __init__(self):
        pass
    def measure_qubits(self, recived_qubits):
        orientations = []
        for i in range(len(recived_qubits)):
            orientations.append(random.randint(0,1))
        for i in range(len(recived_qubits)):
            if(orientations[i] == 0):
                recived_qubits[i].measure("horizontal")
            else:
                recived_qubits[i].measure("vertical")
        return recived_qubits
'''