import numpy as np
import functions as ns
import keys

def hex2bin(hex):
    binary = ""
    for char in hex:
        binary += bin(int(char, 16))[2:].zfill(4)
    return binary

def con64to56(key):
    ans=[]
    for i in range(64):
        j=1
        if i%8!=7:
            ans = np.append(ans,key[i])
    return ans

def cirLeft(arr, shift):
    arr1,arr2=arr[32:],arr[:32]
    arr1=np.roll(arr1,shift)
    arr2=np.roll(arr2,shift)
    return (np.concatenate((arr2,arr1)))

def key_gen(hex_key):
    hex_key=hex2bin(hex_key)
    key=[]
    for char in hex_key:
        key=np.append(key,bin(int(char,2))[2:])
    LSK= con64to56(key)
    rkb=[0]*16
    for i in range(16):
        LSK=cirLeft(LSK,keys.shift[i])
        contraction=ns.permute(LSK,keys.CP,48)
        rkb[i]=hex(int(contraction,2))[2:]
    return rkb

if __name__ == '__main__' :
    key="123bacdf1abfd2a9"
    print(key_gen(key))
    print(len(key_gen(key)[0]))