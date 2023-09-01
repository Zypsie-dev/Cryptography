#interanational data encryption algorithm
import numpy as np
import round as rf
import key_generation as kg

def text_to_hex(text):
        hex_representation = ''.join(format(ord(char), '02X') for char in text)
        return hex_representation

def hex_to_text(hex_string, encoding='utf-8'):
        bytes_object = bytes.fromhex(hex_string)
        text = bytes_object.decode(encoding)
        return text

def IDEA(plain,key):
    #plain text to hex
    plain=text_to_hex(plain)
    cip = []
    cip = np.append(cip,(np.array([plain[i:i+4] for i in range(0, 16, 4)])))
    #round keys generation
    rkeys= kg.key_generation(key)
    #8 round
    for i in range(8):
        cip=rf.round(cip,rkeys[i*6:(i*6)+6])
    #half round
    cip=rf.half_round(cip,rkeys[48:])
    ans=""
    for i in cip:
        ans+=i
    return (ans)


if __name__ == '__main__':
    key="12311237ab7cdef829ba1abdf29af212"
    plain="nabinshr"
    print(IDEA(plain,key))
    print(len(IDEA(plain,key)))

    # Example usage
    hex_representation = "6E6162696E736872"  # Hexadecimal representation of "Hello, World!"
    text = hex_to_text(hex_representation)
    print(text)


    # Example usage
    text = "nabinshr"
    hex_representation = text_to_hex(text)
    print(hex_representation)
    print(len(hex_representation))

