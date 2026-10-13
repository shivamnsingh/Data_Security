import hashlib


def main():
    print("MD5:", hashlib.md5("Hlo, World".encode()).hexdigest())
    try:
        text = input("Enter the value to encode: ")
    except EOFError:
        text = "Hello, World"
    print("The hexadecimal equivalent of SHA-1 is", hashlib.sha1(text.encode()).hexdigest())


if __name__ == "__main__":
    main()
