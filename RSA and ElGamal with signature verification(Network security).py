import math
import random
import hashlib

# RSA============================


def e_calculation(a, b):
    t = 0
    for k in range(a, 100):
        if math.gcd(k, b) == 1:
            t = 1
            return k

        if t == 1:
            k = 100


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m_bar):
    g, x, y = egcd(a, m_bar)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m_bar
# RSA============================


# ElGamal============================
def Find_Generator(x, y, z):
    return pow(x, y, z)


def Generator(p):
    p_d1 = 2
    p_d2 = (p - 1) // p_d1
    while (1):
        g = random.randint(2, p - 1)
        if not (Find_Generator(g, p_d2, p) == 1):
            if not Find_Generator(g, (p - 1) // p_d2, p) == 1:
                return g


def inverseMod(a, m):
    for i in range(1,m):
        if ( m*i + 1) % a == 0:
            return ( m*i + 1) // a
    return None
# ElGamal============================


if __name__ == '__main__':
    print("Type 1 for RSA:")
    print("Type 2 for ElGamal:")
    t = int(input())
    if t == 1:
        # 9255508488585186558329059148455349235297915087215275097633716289
        # 8683264007267738417529408923184363394510874535680657958930341377
        p = int(input("Enter the value of p:"))
        print(p)
        q = int(input("Enter the value of q:"))
        print(q)
        N = p * q
        phi_n = (p - 1) * (q - 1)
        m = int(input("Enter your message:"))
        en_key = e_calculation(2, phi_n)
        print("Public key:", en_key)
        enc = pow(m, en_key, N)
        print("Encrypted message:", enc)
        d = modinv(en_key, phi_n)
        plaintext = pow(enc, d, N)
        print("Plain text:", plaintext)
        v = int(input("Do you want to check signing and verification if yes type 1 else 0"))
        if v == 1:
            h = int(hashlib.sha256("m".encode('UTF-8')).hexdigest(), 16)
            print("Hash value:", h)
            s = pow(h, d, N)
            print("S:", s)
            h2 = pow(s, en_key, N)
            if h == h2:
                print("Valid signature")
            else:
                print("Invalid signature")
    elif t == 2:
        p = int(input("Enter prime:"))
        g = Generator(p)
        print("Generator:", g)

        x = int(input("Enter secret key:"))

        y = pow(g, x, p)
        print("public key:", y)

        m = int(input("Enter message:"))

        r = int(input("Enter random value:"))

        c11 = pow(g, r, p)
        temp_1 = pow(y, r, p)
        temp_2 = (m * temp_1)
        c12 = pow(temp_2, 1, p)
        print("Cypher text 1:", c11)
        print("Cypher text 2:", c12)

        temp1 = pow(c11, x, p)
        inverse = inverseMod(temp1, p)
        temp2 = (c12 * inverse)
        plain_text = pow(temp2, 1, p)
        print("Plain text:", plain_text)

    else:
        print("Invalid, must enter 1 or 2")