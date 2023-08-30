# Binary to decimal conversion
def bin2dec(binary):
    decimal_number = int(binary, 2)
    return decimal_number
 
# Decimal to binary conversion
def dec2bin(num):
    binary_representation = bin(num)
    return(binary_representation[2:])

#Hex to binary conversion
def hex2bin(hexa):
    hex_number = hexa # Input hexadecimal number
    decimal_number = int(hex_number, 16)  # Convert hex to decimal
    binary_representation = bin(decimal_number)  # Convert decimal to binary
    binary_digits = binary_representation[2:]  # Remove '0b' prefix
    return(binary_digits)  # Output: '11010'

# Binary to hexadecimal conversion
def bin2hex(binary):
    decimal_number = int(binary, 2)  # Convert binary to decimal
    hexadecimal_representation = hex(decimal_number)  # Convert decimal to hexadecimal
    hexadecimal_digits = hexadecimal_representation[2:]  # Remove '0x' prefix
    return hexadecimal_digits

# Permute function to rearrange the bits
def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + str(k[arr[i] - 1])
    return permutation

#Xor
def xor(a,b):
    ans=""
    for i in range(len(a)):
        if a[i]==b[i]:
            ans=ans+"0"
        else:
            ans=ans+"1"
    return ans


def convertToArr(num):
    digit_array = [(digit) for digit in num]
    return digit_array

def arr2hex(arr):
    ans=""
    for i in range(0,len(arr),4):
        num_arr=arr[i:i+4]
        num=""
        for j in (num_arr):
            num=num+str(j)
        ans=ans+bin2hex(num)
    return ans

