def encrypt(plaintext,key):
    key_length=len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int=[ord(i) for i in plaintext]
    ciphertext=""
    for i in range(len(plaintext_int)):
        value=(plaintext_int[i]+key_as_int[i%key_length])%26
        ciphertext=ciphertext+chr(value+65)
        return ciphertext

e=encrypt("Hello","Hi")
print(e)
