import logging
import random


HEALTHY_THRESHOLD = 100
POL_DECIMALS = 10**18
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

def mock_eth_get_balance(wallet_address):
    """Simulates a JSON-RPC call to a Polygon Node"""
    if random.random() < 0.2:  # 20% chance the node is 'down'
        return {"error": "Node Timeout", "code": -32000}
    
    # Returns a balance in Wei (e.g., 95 POL)
    return {"jsonrpc": "2.0", "result": "0x487A9A104D200000", "id": 1}

def healthcheck() -> int:
    balance = mock_eth_get_balance(1)
    if balance.get("error"):
        error_msg = f'RPC ERROR | error: {balance.get("error")} | code: {balance.get("code")}'
        logger.error(error_msg)
        return 1
    
    pol = int(balance.get("result"), 16) / (POL_DECIMALS)

    if pol < HEALTHY_THRESHOLD:
        logger.warning(f'LOW FUNDS | wallet_id: {balance.get("id")} | balance: {pol:.2f} | threshold: {HEALTHY_THRESHOLD}')

    return 0

def main():
    # 1. Fetch the balance
    # 2. Convert wei to POL
    # 3. Conditional check for POL value, critical log if < 100
    # 4. Handle API errors gracefully
    healthcheck()
    return

if __name__ == "__main__":
    main()
