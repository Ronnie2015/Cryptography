from random import randrange,random
import random

# declaring necessary functions
def is_prime(num, k=6):
    from random import randint
    if num < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if num % p == 0: return num == p
    s, d = 0, num-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, num-1), d, num)
        if x == 1 or x == num-1: continue
        for r in range(1, s):
            x = (x * x) % num
            if x == 1: return False
            if x == num-1: break
        else: return False
    return True
def generate_prime(num):
    p = 1
    while not is_prime(p):
        p = randrange(num)
    return p

def generateInteger(num):  #n bit Ramdom Prime Number
    return random.randint(2**(num-1), 2**num)

def computeGCD(x, y):
    while (y):
        x, y = y, x % y
    return x

def modInverse(a, m): # Euclid's algo
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('invalid modular inverse ')
    else:
        return (x+m) % m

#chaums blind signature start
#initialization
num=int (input("Enter number of Bit of Prime number:"))

p= generate_prime(2**num)
#p=int(input("Enter Prime P:"))
print("p:",p)
q= generate_prime(2**num)
#q=int(input("Enter Prime q:"))
print("q:",q)

n=p*q
fyN=(p-1)*(q-1)
e= generateInteger(num)
while(computeGCD(e, fyN) != 1):
    e = generateInteger(num)
d= modInverse(e, fyN)

print("Initializing phase:")
print("Private Key: p,q,d= ",p,q,d)
print("Public Key: e,n= ",e,n)

print( "Blinding Phase: ")
tj=int(input("Enter the message: "))
rj= generateInteger(num)
while(computeGCD(rj, n) != 1):
   rj = generateInteger(num)
alpha= pow((pow(rj,e,n)*tj),1,n) #a = rj^e *Tj mod n
print("a =",alpha)

print( "Signing phase: ")
t=pow(alpha,d,n) #t = a^d mod n
print( "t = ",t)

print( "Unblinding phase: ") #  s=t*rj-1 mod n
inv=modInverse(rj,n)
s= pow((t*inv),1,n)
print( "s= ",s)

print( "VerifyNing phase: " )#s^e=tj
final_message=pow(s,e,n)
print( (final_message))
