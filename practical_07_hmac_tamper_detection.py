import hashlib
import hmac


def main():
    key = b"secret-key"
    mac1 = hmac.new(key, b"Transfer $100 to Alice", hashlib.sha256).hexdigest()

    # Different message (Alice -> Bob): MACs differ, tampering detected
    mac2 = hmac.new(key, b"Transfer $100 to Bob", hashlib.sha256).hexdigest()
    print("MAC (sent):    ", mac1)
    print("MAC (received):", mac2)
    print("MACs match?", hmac.compare_digest(mac1, mac2))

    # Tampered amount and recipient
    mac3 = hmac.new(key, b"Transfer $9999 to Bob", hashlib.sha256).hexdigest()
    print("Tampered?", not hmac.compare_digest(mac1, mac3))


if __name__ == "__main__":
    main()
