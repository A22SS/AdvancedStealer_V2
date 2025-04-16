import requests
import time
import hashlib
import random

class APIScraper:
    def __init__(self, api_keys=None):
        self.api_keys = api_keys or ['default_api_key_here']
        self.base_urls = {
            'etherscan': 'api.etherscan.io/api',
            'bscscan': 'api.bscscan.com/api',
        }
        self.endpoints = {
            'address_balance': '?module=account&action=balance',
            'address_tx': '?module=account&action=txlist&startblock=0&endblock=99999999',
        }

    def scrape(self, address):
        results = {}
        for service, base_url in self.base_urls.items():
            for endpoint, params in self.endpoints.items():
                params += f'&address={address}'
                if self.api_keys:
                    params += f'&apikey={random.choice(self.api_keys)}'
                time.sleep(1)
                full_url = f'https://{base_url}{params}'
                try:
                    response = requests.get(full_url, timeout=5)
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('status') == '1' or data.get('message') == 'OK':
                            results[f'{service}_{endpoint}'] = data
                except requests.RequestException as e:
                    print(f"API Request failed for {service}: {e}")
        if results:
            raw_balance = results.get('etherscan_address_balance', {}).get('result', '0')
            wei_balance = float(raw_balance)
            eth_balance = wei_balance / 1e18
            results.update({
                'chain_id': 1,
                'blockchain': 'Ethereum',
                'explorer': 'etherscan.io',
                'balance': {
                    'eth': eth_balance,
                    'wei': wei_balance
                }
            })
            address_hash = hashlib.sha256(address.encode('utf-8')).hexdigest()
            results['address_hash'] = address_hash
        return results

scraper = APIScraper()
