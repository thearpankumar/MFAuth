import secrets
import base64


def generateBase32Key(length):
    random_bytes = secrets.token_bytes(length)
    base32_key = base64.b32encode(random_bytes).decode('utf-8')
    return base32_key


if __name__ == '__main__':
    key = generateBase32Key(20)
    print(f'Generated Base32 Key: {key}')
