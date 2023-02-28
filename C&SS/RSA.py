p  = 7
q = 9
n = p*q
phi = (p-1)*(q-1)
e = 2

def gcd(n1,n2):
    if n2 == 0:
        return n1
    return gcd(n2,n1%n2)
    
while e<phi:
    if gcd(e,phi)==1:
        break
    e+=1

d =  pow(e,-1,phi)
m = None
c = None
print("1.Encrypt 2.Decrypt")
choice = int(input("Choice: "))
if choice==1:
    m = int(input("Message: "))
    if m<n:
        c = pow(m,e)%n
        print(c)
    else:
        print("error: message should be less than {}!".format(n))
        
elif choice==2:
    c = int(input("Cipher: "))
    m = pow(c,d)%n
    print("Message: {}".format(m))
    