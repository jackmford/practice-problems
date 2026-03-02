import time
import requests
from prometheus_client import start_http_server, Gauge, Info

RPC_URL = "https://polygon.drpc.org"
WALLET_ADDRESS = "0x000000000000000000000000000000000000dEaD"
SCRAPE_INTERVAL = 15
PORT = 8000

WALLET_BALANCE = Gauge('relayer_wallet_balance_pol', 'Balance of the relayer wallet in POL', ['address'])
BLOCK_HEIGHT = Gauge('polygon_node_block_height', 'Current block height of the connected RPC node')
RPC_LATENCY = Gauge('polygon_rpc_latency_seconds', 'Latency of the RPC node response')

def fetch_blockchain_data():
    """Talks to Polygon and updates our Prometheus metrics."""
    
    # Fetch Block Height (eth_blockNumber)
    payload_block = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    
    start_time = time.time()
    try:
        response = requests.post(RPC_URL, json=payload_block, timeout=10)
        latency = time.time() - start_time
        RPC_LATENCY.set(latency)
        
        if response.status_code == 200:
            result = response.json().get('result')
            block_num = int(result, 16)
            BLOCK_HEIGHT.set(block_num)
            
        # Fetch Wallet Balance (eth_getBalance)
        payload_balance = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [WALLET_ADDRESS, "latest"],
            "id": 1
        }
        
        balance_res = requests.post(RPC_URL, json=payload_balance, timeout=10)
        if balance_res.status_code == 200:
            wei_bal = int(balance_res.json().get('result'), 16)
            pol_bal = wei_bal / 10**18
            WALLET_BALANCE.labels(address=WALLET_ADDRESS).set(pol_bal)
            
    except Exception as e:
        print(f"SRE Alert: Failed to fetch data: {e}")

if __name__ == '__main__':
    start_http_server(PORT)
    print(f"Exporter started on port {PORT}. Monitoring {WALLET_ADDRESS}...")

    while True:
        fetch_blockchain_data()
        time.sleep(SCRAPE_INTERVAL)
