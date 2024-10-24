import steap_by_steap
import random
from math import gcd
from PIL import Image

chars2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
def caesar_encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    # Convert the image to RGB (if it's not already in that format)
    img = img.convert('RGB')
    pixels = img.load()

    # Apply Caesar cipher on each pixel's RGB values
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Encrypt each channel (R, G, B)
            r_encrypted = (r + key) % 256
            g_encrypted = (g + key) % 256
            b_encrypted = (b + key) % 256
            # Set the encrypted pixel value
            pixels[i, j] = (r_encrypted, g_encrypted, b_encrypted)

    # Save the encrypted image
    img.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def caesar_decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    img = Image.open(input_image_path)
    pixels = img.load()

    # Apply reverse Caesar cipher (decryption) on each pixel's RGB values
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Decrypt each channel (R, G, B)
            r_decrypted = (r - key) % 256
            g_decrypted = (g - key) % 256
            b_decrypted = (b - key) % 256
            # Set the decrypted pixel value
            pixels[i, j] = (r_decrypted, g_decrypted, b_decrypted)

    # Save the decrypted image
    img.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")



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
	print(cifrate,type(cifrate))
	for value in cifrate:
		print(value,d)
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


def binary(binary_text,key="c"):
	
	codes=steap_by_steap.LZWCompress(binary_text)
	encripted=steap_by_steap.EncryptXOR(str(codes),key)


	print(encripted)
	decripted=steap_by_steap.DecryptXOR(encripted,key)
	plaintext=steap_by_steap.LZWDecompress(eval(decripted))
	print(plaintext)
def text(message,rust=1):
	limit = 10  # Set a limit for random prime generation
	key1, key2 = genprimes(limit)  # Generate two random primes
	n, e, deckey = genKey(key1, key2)  # Generate RSA keys

	code,diccionary=steap_by_steap.HuffmanCompress(message)
	print(code)
	if  rust:
		encrypted_msg = steap_by_steap.py_encrypt_rsa(code, e, n)#EncryptRSA
	else:

		encrypted_msg = encryptRsa(code, e, n)
	print(f"Encrypted Message: {encrypted_msg}")
	if rust:
		decrypted_msg = steap_by_steap.py_decrypt_rsa(encrypted_msg, deckey, n)#DecryptRSA
	else:
		decrypted_msg = decryptRsa(encrypted_msg, deckey, n)
	print(f"Decrypted Message: {decrypted_msg}")
	hdecompresed=steap_by_steap.HuffmanDecompress(code,diccionary)
	print(hdecompresed)

def image():
	inimg="1.png"
	outimg="ans.png"
	r=0.23
	steap_by_steap.CompressImageFFT(inimg,outimg,r)
	# Example usage:
	key = 158 # Choose a shift key
	input_image = inimg#'outimg.png'  # Replace with your image path
	encrypted_image = 'encrypted_image.png'
	decrypted_image = 'decrypted_image.png'

	# Encrypt the image
	caesar_encrypt_image(input_image, encrypted_image, key)

	# Decrypt the image
	caesar_decrypt_image(encrypted_image, decrypted_image, key)


#text("mi mama me lava la ropa")
#binary("10101010111000111000111")
image()