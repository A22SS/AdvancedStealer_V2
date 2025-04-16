from binaryornot.check import is_binary
from pycryptsy import keyczar
import os
import json
import base64

class WalletDecryptor:
    def __init__(self):
        self.default_password = b"DefaultPassword123!"

    def decrypt(self, encrypted_data, password=None):
        if password is None:
            password = self.default_password
        is_binary_file = is_binary(encrypted_data)
        if is_binary_file:
            if len(encrypted_data) in [279, 280]:
                return encrypted_data[35:-4].decode('utf-8')
        else:
            try:
                wallet_data = json.loads(encrypted_data)
                crypto_type = wallet_data.get('crypto', {}).get('kdf', {}).get('type', '')
                if crypto_type == 'scrypt':
                    import scrypt
                    salt = bytes.fromhex(wallet_data['crypto']['kdfparams']['salt'])
                    dklen = wallet_data['crypto']['kdfparams']['dklen']
                    n = wallet_data['crypto']['kdfparams']['n']
                    r = wallet_data['crypto']['kdfparams']['r']
                    p = wallet_data['crypto']['kdfparams']['p']
                    key = scrypt.hash(password, salt, n=n, r=r, p=p, dklen=dklen)
                    crypter = keyczar.Crypter.Read(os.path.join('keys', 'aes'))
                    decrypted_data = crypter.Decrypt(key.encode('utf-8'), base64.b64decode(wallet_data['crypto']['ciphertext']))
                    return json.loads(decrypted_data)
                elif crypto_type.startswith('pbkdf2'):
                    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
                    from cryptography.hazmat.primitives import hashes
                    salt = bytes.fromhex(wallet_data['crypto']['kdfparams']['salt'])
                    iterations = wallet_data['crypto']['kdfparams']['c']
                    dklen = wallet_data['crypto']['kdfparams']['dklen']
                    key = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=dklen,
                        salt=salt,
                        iterations=iterations,
                    ).derive(password)
                    return keyczar.Crypter.Read(os.path.join('keys', 'aes')).Decrypt(key, base64.b64decode(wallet_data['crypto']['ciphertext']))
            except (json.JSONDecodeError, KeyError):
                return "Failed to decrypt due to JSON formatting or key errors"

decryptor = WalletDecryptor()
