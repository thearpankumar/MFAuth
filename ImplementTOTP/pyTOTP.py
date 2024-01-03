import base64
import hmac
import struct
import qrcode
import time


def HMAC(key, counter, digits=6, digest='sha256'):
    key = base64.b32decode(key.upper() + '=' * ((8 - len(key)) % 8))
    counter = struct.pack('>Q', counter)
    mac = hmac.new(key, counter, digest).digest()
    offset = mac[-1] & 0x0f
    binary = struct.unpack('>L', mac[offset:offset+4])[0] & 0x7fffffff
    return str(binary)[-digits:].zfill(digits)

def TOTP(key, time_step=30, digits=6, digest='sha256'):
    return HMAC(key, int(time.time() / time_step), digits, digest)

def generateQR(secret, app_name='qrTOTP', filename='./ImplementTOTP/qrcode.png', algorithm='sha256'):
    uri = f'otpauth://totp/{app_name}?secret={secret}&algorithm={algorithm.upper()}'
    img = qrcode.make(uri)
    img.save(filename)
    print(f'QR code for {app_name} saved as {filename}')
    img.show()

def main():
    app_name = 'qrTOTP'  
    secret_key = input(f"Enter your secret key for {app_name}: ").strip()
    
    while not secret_key:
        print("Secret key cannot be empty.")
        secret_key = input(f"Enter your secret key for {app_name}: ").strip()

    TOTP_value = TOTP(secret_key)
    print(f'TOTP for {app_name}: {TOTP_value}')
    
    generateQR(secret_key, app_name)

if __name__ == '__main__':
    main()
