import rsa as rsa_lib  # pip package "rsa"


def main():
    public_key, private_key = rsa_lib.newkeys(512)
    signature = rsa_lib.sign("Data Security Practical".encode(), private_key, "SHA-256")
    print("Digital Signature Created")

    for message in ("Data Security Practical", "Data Security Practical Exam"):
        try:
            rsa_lib.verify(message.encode(), signature, public_key)
            print(f"{message!r}: the signature is valid.")
        except rsa_lib.VerificationError:
            print(f"{message!r}: the signature is not valid.")


if __name__ == "__main__":
    main()
