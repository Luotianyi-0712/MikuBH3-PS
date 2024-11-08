import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt_ecb(key: str, data: str):
    cipher = AES.new(bytes.fromhex(key.replace(" ", "")), AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode()


def decrypt_ecb(key: str, data: str):
    data = base64.b64decode(data)
    cipher = AES.new(bytes.fromhex(key.replace(" ", "")), AES.MODE_ECB)
    decrypted = cipher.decrypt(data)
    return unpad(decrypted, AES.block_size).decode()
