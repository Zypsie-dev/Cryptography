""" 
    STEPS:
    1.Multiply X1 with Z1.
    2.Add X2 to Z2.
    3.Add X3 to Z3.
    4.Multiply X4 with Z4.
    5.Bitwise XOR the results of steps 1 and 3.
    6.Bitwise XOR the results of steps 2 and 4.
    7.Multiply the result of step 5 with Z5.
    8.Add the results of steps 6 and 7.
    9.Multiply the result of step 8 with Z6.
    10.Add the results of steps 7 and 9.
    11.Bitwise XOR the results of steps 1 and 9.
    12.Bitwise XOR the results of steps 3 and 9.
    13.Bitwise XOR the results of steps 2 and 10.
    14.Bitwise XOR the results of steps 4 and 10.
"""

def add(a, b):
    a=int(a,16)
    b=int(b,16)
    return hex((a + b) % (2 ** 16))[2:]

def multiply(a, b):
    a=int(a,16)
    b=int(b,16)
    return hex((a * b) % ((2 ** 16) + 1))[2:]

def round(x,keys):
    x1 = multiply(x[0], keys[0]) # x1 = x1*k1
    x2 = add(x[1], keys[1])      # x2 = x2+k2
    x3 = add(x[2], keys[2])      # x3 = x3+k3
    x4 = multiply(x[3], keys[3]) # x4 = x4*k4
    xor1 = hex(int(x1, 16) ^ int(x3, 16))[2:]   # xor1 = x1^x3
    xor2 = hex(int(x2, 16) ^ int(x4, 16))[2:]   # xor2 = x2^x4
    xor1 = multiply(xor1, keys[4])   # xor1 = xor1*k5
    xor2 = add(xor2, xor1)        # xor2 = xor2+xor1
    xor2 = multiply(xor2, keys[5])   # xor2 = xor2*k6
    xor1 = add(xor1, xor2)      # xor1 = xor1+xor2
    x1=hex(int(x1,16)^int(xor1,16))[2:] # x1 = x1^xor1
    x3=hex(int(x3,16)^int(xor1,16))[2:] # x3 = x3^xor1
    x2=hex(int(x2,16)^int(xor2,16))[2:] # x2 = x2^xor2
    x4=hex(int(x4,16)^int(xor2,16))[2:] # x4 = x4^xor2
    return [x1,x3,x2,x4]

def half_round(x,keys):
    x1 = multiply(x[0], keys[0]) # x1 = x1*k1
    x2 = add(x[1], keys[1])      # x2 = x2+k2
    x3 = add(x[2], keys[2])      # x3 = x3+k3
    x4 = multiply(x[3], keys[3]) # x4 = x4*k4
    return [x1,x3,x2,x4]




