def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


def RSA(data, mode):
    p = 11
    q = 13
    n = p*q
    phi = (p-1)*(q-1)
    e = 2

    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = pow(e, -1, phi)

    if mode == 0:
        return pow(data, e) % n
    elif mode == 1:
        return pow(data, d) % n


m = None
c = None
print("1.Encrypt 2.Decrypt")
choice = int(input("Choice: "))
if choice == 1:
    m = list(input("Message: "))
    a = list(map(lambda char: ord(char.upper()), m))
    c = [RSA(i, 0) for i in a]
    print("Cipher: {}".format(c))

elif choice == 2:
    c = input("Cipher: ").split(",")
    temp = [RSA(int(i), 1) for i in c]
    m = "".join(list(map(lambda char: chr(char), temp)))
    print("Message: {}".format(m))
