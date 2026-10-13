from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(key, text):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(text.encode(), AES.block_size))


def aes_decrypt(key, cipher_text):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(cipher_text), AES.block_size).decode()


def main():
    key, text = b"mysecretkey12345", "Everyone"
    cipher_text = aes_encrypt(key, text)
    print("Cipher (hex):", cipher_text.hex())
    print("Plain Text:", aes_decrypt(key, cipher_text))


if __name__ == "__main__":
    main()
