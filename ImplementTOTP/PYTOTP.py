import base64
import hmac
import struct
import qrcode
import time
from base32Key import generateBase32Key


class PYTOTP:

    def __init__(self):
        self.key32 = generateBase32Key(20)

    def hmac(self, key, counter, digits, digest):
        key = base64.b32decode(key.upper() + '=' * ((8 - len(key)) % 8))
        counter = struct.pack('>Q', counter)
        mac = hmac.new(key, counter, digest).digest()
        offset = mac[-1] & 0x0f
        binary = struct.unpack('>L', mac[offset:offset + 4])[0] & 0x7fffffff
        return str(binary)[-digits:].zfill(digits)

    def current_time_totp(self, key, time_step=30, digits=6, digest='sha256'):
        return self.hmac(key, int(time.time() / time_step), digits, digest)

    def generateqr(self, secret, app_name='qrTOTP', filename='qrcode.png', algorithm='sha256'):
        uri = f'otpauth://totp/{app_name}?secret={secret}&algorithm={algorithm.upper()}'
        img = qrcode.make(uri)
        img.save(filename)
        print(f'QR code for {app_name} saved as {filename}')
        img.show()

    def get_totp_at_time(self, key, timestamp, time_step=30, digits=6, digest='sha256'):
        counter = int(timestamp / time_step)
        return self.hmac(key, counter, digits, digest)

    def get_multiple_totp_values(self, key):
        current_time = int(time.time())
        one_minute_back = current_time - 60
        three_seconds_back = current_time - 3
        next_30_seconds = current_time + 30
        next_one_minute = current_time + 60

        totp_values = [
            self.get_totp_at_time(key, one_minute_back),
            self.get_totp_at_time(key, three_seconds_back),
            self.current_time_totp(key),
            self.get_totp_at_time(key, next_30_seconds),
            self.get_totp_at_time(key, next_one_minute),
        ]


if __name__ == '__main__':
    print(generateBase32Key(20))
    app_name = 'qrTOTP'
    secret_key = input(f"Enter your secret key for {app_name}: ").strip()

    while not secret_key:
        print("Secret key cannot be empty.")
        secret_key = input(f"Enter your secret key for {app_name}: ").strip()

    totp_instance = PYTOTP()

    # print(f' TOTP for {app_name}: {TOTP_value}')
    print(""" What do you want to do with your TOTP \n 
        1. Generate the TOTP code for your secret : \n
        2. Check your code generated from app : \n
        3. Generate Qrcode for your secret : """)

    choice = int(input("Enter your choice : "))
    if choice == 1:
        TOTP_value = totp_instance.current_time_totp(secret_key)
        print(TOTP_value)
    elif choice == 2:
        counter = 0
        otp = int(input("Enter your OTP : "))
        while otp in totp_instance.get_multiple_totp_values():
            print("otp is correct for authentication .")
            counter += 1
            if counter == 5:
                break
        else:
            print("TRY AGAIN LATER PROPERLY")
    elif choice == 3:
        totp_instance.generateqr(secret_key, app_name)
    else:
        print("Invalid")