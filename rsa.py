import random
from math import gcd

chars2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def publicKeyE(fi):
	e = 0
	for i in range(2,fi):
		if  gcd(fi,i) == 1 :
			e = i
			break
	return e
def privateKeyD(e,fi):
	i = 2
	while True:
		formula = (1+fi*i)%e
		d = int((1+fi*i)/e)
		if (formula == 0 and d != e):
			return d
		i += 1
def genprimes(limit):
    prime1 = getrndPrime(limit)
    prime2 = getrndPrime(limit)
    return prime1, prime2
def genKey(key1,key2):
	n = key1 * key2
	fi = (key1 - 1 ) * (key2 - 1 )
	base = key1 * key2 - key1 - key2 + 1 
	publica = publicKeyE(fi)
	privada = privateKeyD(publica , fi)
	return n , publica , privada
def encryptRsa(msg,e,n):
	cifrate = []
	for i in msg:	
		value = int(chars2.index(i))
		enchar = (value**int(e))%int(n)
		cifrate.append(enchar)
	return cifrate
def decryptRsa(cifrate,d,n):
	msg = ""
	d = int(d)
	n = int(n)
	cifrate = eval(str(cifrate))
	for value in cifrate:
		dechar = int((int(value)**d)%n)
		msg += chars2[dechar]
	return msg
# Assuming you have a predefined set of characters for encryption/decryption

def getrndPrime(limit):
    # Generate a random prime number less than the specified limit
    while True:
        num = random.randint(2, limit)
        if is_prime(num):
            return num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():


if __name__ == "__main__":
    main()
