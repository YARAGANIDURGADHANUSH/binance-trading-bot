import typer

def validate_inputs(symbol, side, order_type, quantity, price):
    if side.upper() not in ["BUY", "SELL"]:
        raise typer.BadParameter("Side must be BUY or SELL.")
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise typer.BadParameter("Order type must be MARKET or LIMIT.")
    if quantity <= 0:
        raise typer.BadParameter("Quantity must be positive.")
    if order_type.upper() == "LIMIT" and not price:
        raise typer.BadParameter("Price is required for LIMIT orders.")
    return True
