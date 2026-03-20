from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        # Initializing the client with Testnet enabled
        self.client = Client(api_key, api_secret, testnet=True)
        # Using the specific testnet URL required by the assignment
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'

    def send_order(self, symbol, side, order_type, quantity, price=None):
        # Dictionary to hold our order parameters
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        # Logic for Limit orders
        if order_type.upper() == "LIMIT":
            if not price:
                raise ValueError("Limit orders require a price!")
            params["price"] = str(price)
            params["timeInForce"] = "GTC" # Standard: Good Till Cancelled

        return self.client.futures_create_order(**params)
