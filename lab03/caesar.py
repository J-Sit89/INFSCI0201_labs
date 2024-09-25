class Caesar:
    def __init__(self):
        """Initialize the Caesar object with a default key of 0."""
        self.__key = 0  
    
    def set_key(self, key):
        """Set the encryption/decryption key."""
        self.__key = key
    
    def get_key(self):
        """Return the current key."""
        return self.__key
    
    def __shift_char(self, char, shift_amount):
        """
        Shift a single character by the shift amount, handling wrap-around.
        
        Non-alphabetic characters are shifted by their ASCII values.
        """
        if char.isalpha(): 
            shifted = ord(char.lower()) + shift_amount
            if shifted > ord('z'):  
                shifted -= 26
            elif shifted < ord('a'):  
                shifted += 26
            return chr(shifted)
        else: 
            return chr((ord(char) + shift_amount) % 128)  
    
    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using the modified Caesar Cipher.
        
        Preserves whitespace and shifts non-alphabetic characters.
        """
        ciphertext = ''
        for char in plaintext:
            if char == ' ':  
                ciphertext += ' '
            else:
                ciphertext += self.__shift_char(char, self.__key)
        return ciphertext
    
    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext back to plaintext.
        
        Preserves whitespace and shifts non-alphabetic characters.
        """
        plaintext = ''
        for char in ciphertext:
            if char == ' ': 
                plaintext += ' '
            else:
                plaintext += self.__shift_char(char, -self.__key)
        return plaintext


cipher = Caesar()
cipher.set_key(3)
print(cipher.encrypt("hello WORLD!"))  # Output: khoor zruog$
print(cipher.decrypt("khoor zruog$"))  # Output: hello world!

cipher.set_key(6)
print(cipher.encrypt("zzz"))  # Output: fff
print(cipher.decrypt("FFF"))  # Output: zzz

cipher.set_key(-6)
print(cipher.encrypt("FFF"))  # Output: zzz

"""Unsure of where to find style guide where the lab says it should be, so i followed PEP 8 standards"""
