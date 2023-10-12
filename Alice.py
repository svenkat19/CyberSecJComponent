import random
from qubit import Qubit

class Alice:
    def __init__(self):
        self.bits = []
        self.orientations = []
        self.key = []

    def reset(self):
        self.bits = []
        self.orientations = []
        self.key = []

    def measure_qubits(self, received_qubits):
        self.orientations = [random.randint(0, 1) for _ in range(len(received_qubits))]
        self.bits = [received_qubits[i].measure("horizontal" if self.orientations[i] == 0 else "vertical") for i in range(len(received_qubits))]
        return self.orientations

    def create_key(self, indexes_of, length):
        self.key = [self.bits[i] for i in indexes_of]
        byte_array = []

        for i in range(0, len(self.key), 8):
            tmp = ''.join(map(str, self.key[i:i+8]))
            byte_array.append(int(tmp, 2))

        return byte_array



'''import random
from qubit import Qubit
class Alice(object):
    bits = []
    orientations = []
    key = []
    def __init__(self):
        pass
    def reset(self):
        self.bits = []
        self.orientations = []
        self.key = []
    def measure_qubits(self, recived_qubits):
        for i in range(len(recived_qubits)):
            self.orientations.append(random.randint(0,1))
        for i in range(len(recived_qubits)):
            if(self.orientations[i] == 0):
                self.bits.append(recived_qubits[i].measure("horizontal"))
            else:
                self.bits.append(recived_qubits[i].measure("vertical"))
        return self.orientations
    def create_key(self, indexes_of, length):
        for i in indexes_of:
            self.key.append(self.bits[i])
        byte_array = []
        try:
            for i in range(0,99999999,8):
                tmp = ""
                for b in range(8):
                    tmp += str(self.key[i+b])
                byte_array.append(int(tmp,2))
                if(len(byte_array) == length):
                    break
        except:
         pass
        return byte_array

'''