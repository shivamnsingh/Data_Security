from cryptography.hazmat.primitives.asymmetric import ec


def main():
    a_priv = ec.generate_private_key(ec.SECP256R1())
    b_priv = ec.generate_private_key(ec.SECP256R1())
    a_secret = a_priv.exchange(ec.ECDH(), b_priv.public_key())
    b_secret = b_priv.exchange(ec.ECDH(), a_priv.public_key())
    print("Keys Match?", a_secret == b_secret)


if __name__ == "__main__":
    main()
