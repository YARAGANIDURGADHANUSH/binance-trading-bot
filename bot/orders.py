from bot.logging_config import setup_bot_logging

logger = setup_bot_logging()

def place_new_order(client, symbol, side, order_type, quantity, price):
    try:
        logger.info(f"Attempting {order_type} {side} for {symbol}")
        
        # Calling the client wrapper
        response = client.send_order(symbol, side, order_type, quantity, price)
        
        # Logging details for the assignment requirements
        logger.info(f"Order Successful! ID: {response.get('orderId')}")
        return response

    except Exception as e:
        logger.error(f"Order Failed! Reason: {str(e)}")
        return {"error": str(e)}
