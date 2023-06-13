from random import randrange, random
import random
import uuid
import hashlib
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()# + ':' + salt

def is_prime(n, k=6):
    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True
def randprime(N=10**40):
    p = 1
    while not is_prime(p):
        p = randrange(N)
    return p
ID = []
passwards = []
p_bar = []
binaryPbar = []
r = []
rBinary = []
Q =[]
rBar =[]
#hash_random2 = []
if __name__ == '__main__':
    numberOfItems = int(input("enter the number of items in the list : "))
    for i in range(numberOfItems) :
        d = randprime(2 ** 20)
        ID.append(d)
    print("This is the ID list that Clint sneds to Server",ID)
    d = int(input("enter your ID :  "))
    for j in range(numberOfItems) :
        if ID[j] == d :
            print("my ID : ",ID[j])
            myID = ID[j]
            positions = j
            break
    for k in range(numberOfItems):
        p = randrange(2**20)
        passwards.append(p)
        if positions == k:
            myPassward = passwards[k]
    print("This is passward list for corresponding IDs",passwards)
    print("This is my passward : ", myPassward)
    for t in range(numberOfItems):
        hashed_password = (hash_password(str(passwards[t])))
        p_bar.append(hashed_password)
        word =str(p_bar[t])
        byte_arr = bytearray(word, 'utf8')
        res = []
        for byte in byte_arr:
            binary_rep = bin(byte)
            res.append(binary_rep[2:])
        b = ''.join(res)
        binaryPbar.append(int(b))
    print("This is p' list ",p_bar)
    print("this is the binary value of p' ",binaryPbar)
    for rs in range(numberOfItems):
        word = str(randprime(2 ** 20))
        rBar.append(word)
        byte_arr = bytearray(word, 'utf8')
        res = []
        for byte in byte_arr:
            binary_rep = bin(byte)
            res.append(binary_rep[2:])
        b = ''.join(res)
        r.append(int(b))
    print("This is the random string ",r)
    for xor in range(numberOfItems):
        q =(binaryPbar[xor])^(r[xor])
        Q.append(q)
    print("this is passward lsit P send to clint : ",Q)
    for hr in range(numberOfItems) :
        hashed_password = (hash_password(str(r[hr])))
        rBar.append(hashed_password)
    print("this is r bar that is send to clint",rBar)
    PBarPrime = (hash_password(str(myPassward)))
    print("this PBarPrime ",PBarPrime)
    for u in range(numberOfItems):
        if u == positions:
            word = str(PBarPrime)
            byte_arr = bytearray(word, 'utf8')
            res = []
            for byte in byte_arr:
                binary_rep = bin(byte)
                res.append(binary_rep[2:])
            b1 = ''.join(res)
            print("binary of PBarPrime ",b1)
            b3 = Q[u]
            print("this is the value of Q for the clint",b3)
            word = str(b3)
            byte_arr = bytearray(word, 'utf8')
            res = []
            for byte in byte_arr:
                binary_rep = bin(byte)
                res.append(binary_rep[2:])
                b4 = ''.join(res)
            rPrime = int(b1) ^ int(b4)
    print("this is the valur of RPrime ",rPrime)
    rPrimeBar=hashed_password = (hash_password(str(rPrime)))
    print("This the value of rPrimeBar",rPrimeBar)
    for q in range(numberOfItems):
        if rBar[q] == rPrimeBar :
            print("the clint is ready to send r prime")
            break
        else:
            print("This is not ready for sending")




