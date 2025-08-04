import time


start = time.time()
print("Start time:", time.ctime(start))

for i in range(1000000):
    pass

def cipher(plaintext, shift):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ""

    for char in plaintext.lower():  
        if char in alphabet:
            current_index = alphabet.find(char)
            new_index = (current_index + shift) % 26
            new_char = alphabet[new_index]
            
            ciphertext += new_char
        else:
            ciphertext += char
    
    return ciphertext
   


message = "hello world852"
encrypted_message = cipher(message, 3)

print(f"Original message: {message}")
print("Encrypted message:" , encrypted_message)

end = time.time()
print("End time:", time.ctime(end))

print("Execution time:", end - start, "seconds")