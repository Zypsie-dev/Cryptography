import numpy as np

def hex2bin(hex):
    binary = ""
    for char in hex:
        binary += bin(int(char, 16))[2:].zfill(4)
    return binary

def cirLeft(n, shift):
    s = str(n)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]

# Key generation
def key_generation(key):
    key = hex2bin(key)
    keys = []
    #generates 48 keys for 8 rounds
    for j in range(0,48,8):
        keys = np.append(keys,(np.array([hex(int(key[i:i+16],2))[2:] for i in range(0, 128, 16)])))
        cirLeft(key, 25)
    keys = np.append(keys,(np.array([hex(int(key[i:i+16],2))[2:] for i in range(0, 128, 16)]))) #last 4 keys for half round total 52 keys
    return keys




if __name__ == '__main__':
    key="12311237ab7cdef829ba1abdf29af212"
    print(len(key))
    print(key_generation(key))
    print(len(key_generation(key)))
    
