def shift_character(c, shift, alphabet):
    if c not in alphabet:
        return c
    shifted_index = (alphabet.index(c) + shift) % len(alphabet)
    return alphabet[shifted_index]

def caesar_encrypt(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text_lower = text.lower()
    encrypted = ''.join(shift_character(c, shift, alphabet) for c in text_lower)
    return ''.join(e.upper() if t.isupper() else e for t, e in zip(text, encrypted))

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    encrypted = caesar_encrypt("Hello, World!", 3)
    print(f"Encrypted: {encrypted}")
    decrypted = caesar_decrypt(encrypted, 3)
    print(f"Decrypted: {decrypted}")
