import numpy as np
import functions as ns
import keys
import key_generator as kg
import round_func as rf

def des(plain,key):
    cip= ns.convertToArr(plain)
    key=ns.convertToArr(key)

    #round keys generation
    rkeys= kg.key_gen(key)

    #initial Permutation
    cip=ns.permute(cip,keys.IP,keys.IP_len)

    #16 round 
    cip=rf.round_func(cip,rkeys)

    #swapping
    cip_l,cip_r = cip[32:], cip[:32]
    cip = cip_l + cip_r

    #final_permutation
    cip=ns.permute(cip,keys.FP,64)

    #conversion of bin to hex
    cip=ns.arr2hex(cip)

    return cip


test=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
testkey=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
print(des(test,testkey))
print(len(des(test,testkey)))