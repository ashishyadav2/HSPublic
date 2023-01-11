def cipherFunction(key):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char)+key-65) % 26+65)
        else:
            cipher_text += chr((ord(char)+key-97) % 26+97)
    return cipher_text


while True:
    print("\n1.Encrypt 2.Decrypt")
    choice = int(input("Your choice: "))

    if choice == 1:
        plain_text = str(input("Plain text: "))
        key = int(input("Key: "))
        print(cipherFunction(key))

    elif choice == 2:
        plain_text = str(input("Plain text: "))
        key = int(input("Key: "))
        print(cipherFunction(-key))

    else:
        print("Invalid choice!")
        exit()