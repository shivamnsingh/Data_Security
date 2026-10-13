from Crypto.Cipher import DES


def des_encrypt(key, text):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(text.encode())  # text must be a multiple of 8 bytes


def des_decrypt(key, cipher_text):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(cipher_text).decode().strip()


def main():
    key, text = b"mynewkey", "Everyone"
    cipher_text = des_encrypt(key, text)
    print("Cipher:", cipher_text)
    print("Plain Text:", des_decrypt(key, cipher_text))


if __name__ == "__main__":
    main()
