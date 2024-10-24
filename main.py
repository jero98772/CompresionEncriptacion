import steap_by_steap
from rsa import *
def binary():
	c=steap_by_steap.LZWCompress("100110010")
	print(c)
	d=steap_by_steap.LZWDecompress(c)

def text():

	d,hc=steap_by_steap.HuffmanCompress("hellooo")
	hd=steap_by_steap.HuffmanDecompress(d,hc)
	print(hc,hd,d)

	limit = 100  # Set a limit for random prime generation
	key1, key2 = genprimes(limit)  # Generate two random primes
	n, e, d = genKey(key1, key2)  # Generate RSA keys

	print(f"Public Key (n, e): ({n}, {e})")
	print(f"Private Key (d): {d}")

	# Example message to encrypt
	message = "HELLO"
	print(f"Original Message: {message}")

	# Encrypt the message
	encrypted_msg = encryptRsa(message, e, n)
	print(f"Encrypted Message: {encrypted_msg}")

	# Decrypt the message
	decrypted_msg = decryptRsa(encrypted_msg, d, n)
	print(f"Decrypted Message: {decrypted_msg}")
def image():
    d,hc=steap_by_steap.HuffmanCompress("hellooo")
    hd=steap_by_steap.HuffmanDecompress(d,hc)
    print(hc,hd)

    inimg="1.jpg"
    outimg="ans.jpg"
    r=0.99
    steap_by_steap.CompressImageFFT(inimg,outimg,r)


text()