from cryptography.hazmat.primitives.asymmetric import ec


def main():
    """Man-in-the-middle: Bob's side is computed with the attacker's key, so secrets differ."""
    a_priv = ec.generate_private_key(ec.SECP256R1())
    b_priv = ec.generate_private_key(ec.SECP256R1())
    hacker_priv = ec.generate_private_key(ec.SECP256R1())
    intercepted_pub_key = hacker_priv.public_key()

    a_secret = a_priv.exchange(ec.ECDH(), b_priv.public_key())
    b_secret = b_priv.exchange(ec.ECDH(), intercepted_pub_key)  # Bob gets the hacker's key
    print("Do the shared keys match? :", a_secret == b_secret)


if __name__ == "__main__":
    main()
