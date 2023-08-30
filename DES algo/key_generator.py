import numpy as np
import functions as ns
import keys

def con64to56(key):
    ans=[0]*56
    for i in range(64):
        j=0
        if i%8!=7:
            ans[j]=key[i]
    return ans

def cirLeft(arr, shift):
    arr1,arr2=arr[32:],arr[:32]
    arr1=np.roll(arr1,shift)
    arr2=np.roll(arr2,shift)
    return (np.concatenate((arr2,arr1)))

def key_gen(key):
    LSK= con64to56(key)
    rkb=[0]*16
    for i in range(16):
        LSK=cirLeft(LSK,keys.shift[i])
        contraction=ns.permute(LSK,keys.CP,48)
        rkb[i]=contraction
    return rkb
