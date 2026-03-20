import typer
from bot.client import BinanceClient
from bot.orders import place_new_order

app = typer.Typer()

# INSERT YOUR TESTNET KEYS HERE
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

@app.command()
def main(
    symbol: str = typer.Option(..., help="Symbol like BTCUSDT"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option("MARKET", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Amount to trade"),
    price: float = typer.Option(None, help="Required for LIMIT orders")
):
    """
    Simple CLI for Binance Futures Testnet Trading
    """
    client = BinanceClient(API_KEY, API_SECRET)
    
    # Run the order logic
    result = place_new_order(client, symbol, side, order_type, quantity, price)
    
    # Final output to CLI
    if "orderId" in result:
        typer.secho(f"Success: Order {result['orderId']} is {result['status']}", fg="green")
    else:
        typer.secho(f"Failure: {result.get('error')}", fg="red")

if __name__ == "__main__":
    app()
