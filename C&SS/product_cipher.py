import math
def format_string(string):
        return string.replace(" ","").upper()

def cipherFunction(key,plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char)+key-65) % 26+65)
        else:
            cipher_text += chr((ord(char)+key-97) % 26+97)
    return cipher_text

def encipher_rail_fence(text,depth):
    length = len(text)
    c = int(math.ceil(length/depth))
    matrix = [[0 for i in range(c)] for i in range(depth)]
    k = 0
    ans = ""
    for i in range(0,c):
        for j in range(0,depth):
            if k< length:
                matrix[j][i] = text[k]
                k=k+1
               
            else:
                matrix[j][i] = 'X'
    
    for num in matrix:
        print("[",end="")
        for n in num:
            print(" "+n+" ",end="")
            ans+=n
        print("]")
    
    return ans

def decipher_rail_fence(text,depth):
    length = len(text)
    c = int(math.ceil(length/depth))
    matrix = [[0 for i in range(c)] for i in range(depth)]
    k = 0
    ans = ""
    for i in range(0,depth):
        for j in range(0,c):
            if k< length:
                matrix[i][j] = text[k]
                k=k+1
               
            else:
                matrix[i][j] = 'X'
    
    for i in range(0,c):
        for j in range(0,depth):
            print(matrix[j][i])
    
    return ans
    
print("\n1.Encrypt 2.Decrypt")
choice = int(input("Your choice: "))

if choice == 1:
    print("\n1.Substitution->Transposition 2.Transposition->Substitution")
    choice = int(input("Your choice: "))
    if choice == 1:
        plain_text = str(input("Plain text: "))
        key = int(input("Key: "))
        temp = cipherFunction(key,plain_text)
        print("Caeser CT: {}".format(temp))
        depth = int(input("Depth: "))
        print("Cipher Text: {}".format(encipher_rail_fence(temp,depth)))
    
    if choice == 2:
        plain_text = str(input("Plain text: "))
        depth = int(input("Depth: "))
        temp = format_string(plain_text)
        ct = encipher_rail_fence(temp,depth)
        print("Rail Fence CT: {}".format(ct))
        key = int(input("Key: "))
        finalCt = cipherFunction(key,ct)
        print("Cipher Text: {}".format(finalCt))

if choice == 2:
    print("\n1.Substitution->Transposition 2.Transposition->Substitution")
    choice = int(input("Your choice: "))
    if choice == 1:
        plain_text = str(input("Cipher text: "))
        depth = int(input("Depth: "))
        temp = decipher_rail_fence(plain_text,depth)
        key = int(input("Key: "))
        finalPT = cipherFunction(-key,temp)
        print("Plain Text: {}".format(finalPT))
        
    if choice == 2:
        plain_text = str(input("Cipher text: "))
        key = int(input("Key: "))
        temp = cipherFunction(-key,plain_text)
        depth = int(input("Depth: "))
        finalPT = decipher_rail_fence(temp,depth)
        print("Plain Text: {}".format(finalPT))
