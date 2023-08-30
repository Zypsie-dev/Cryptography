# Description: This file contains the round function of the DES algorithm.
import keys
import functions as ns
import numpy as np

def sbox_transform(arr):
    sbox_str = ""
    for j in range(8):
        row = int(ns.bin2dec((str(arr[j * 6]) + str(arr[j * 6 + 5]))))
        col = int(ns.bin2hex((str(arr[j * 6 + 1]) + str(arr[j * 6 + 2]) + str(arr[j * 6 + 3]) + str(arr[j * 6 + 4]))),16)
        num = ns.dec2bin(keys.sbox[j][row][col])
        if len(num)<4:
            for i in range(4-len(num)):
                num="0"+str(num)
        sbox_str = sbox_str + (num)
    return ns.convertToArr(sbox_str)


def mangler_func(arr,rkey):
    rkey=ns.convertToArr(rkey)
    arr = ns.permute(arr, keys.E, 48)
    arr = ns.xor(arr, rkey)
    arr = sbox_transform(arr)
    arr = ns.permute(arr, keys.P, 32)
    return arr

def round_func(arr,rkeys):
    l=arr[:32]
    r=arr[32:]
    for i in range(16):
        temp=r
        r=ns.xor(mangler_func(r,rkeys[i]),l)
        l=temp
    return l+r



