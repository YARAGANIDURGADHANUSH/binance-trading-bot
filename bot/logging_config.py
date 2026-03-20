import logging

def setup_bot_logging():
    # Standard intern-level logging setup
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("bot.log"), # Saves to file for submission
            logging.StreamHandler()        # Prints to console for debugging
        ]
    )
    return logging.getLogger("TradingBot")
