from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def main():
    priv = rsa.generate_private_key(65537, 2048)
    pub = priv.public_key()
    oaep = padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None)

    cipher = pub.encrypt(b"My social security number", oaep)
    print("Ciphertext:", cipher[:20], "...")
    decrypted = priv.decrypt(cipher, oaep)
    print("Decrypted:", decrypted)
    print("Decrypted:", decrypted.decode("utf-8"))


if __name__ == "__main__":
    main()
