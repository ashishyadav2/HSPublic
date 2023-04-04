print("Public Keys")
P = int(input("User1 (P): "))
G = int(input("User2 (G): "))

print("-------------")
print("Private Keys")
a = int(input("User1 (a): "))
b = int(input("User2 (b): "))

x = pow(G, a) % P
y = pow(G, b) % P

Ka = pow(y, a) % P
Kb = pow(x, b) % P

print("-------------")
print("Shared key is {}".format(Ka))
