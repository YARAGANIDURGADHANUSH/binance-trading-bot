# 🤖 Binance Futures Trading Bot

A robust, CLI-based trading bot built in Python to interact with the Binance Futures Testnet. This project demonstrates modular architecture, secure API handling, and automated trade execution.

## 🚀 Project Overview

This application provides a seamless command-line interface to execute and manage trades on the Binance Futures Testnet without risking real capital. It features:
* Modular separation of concerns (API Client, Execution Logic, and CLI)
* Execution of both MARKET and LIMIT orders
* Real-time position and balance checking
* Robust error handling for API limits and invalid parameters
* Structured logging to track all trade lifecycles

## 🧠 Tech Stack

* **Python 3.x** – Core programming language
* **Typer** – For building a clean, user-friendly Command Line Interface (CLI)
* **python-binance** – Official Binance API wrapper for Python
* **Logging** – Built-in Python logging for execution tracking
* **python-dotenv** – Secure environment variable management

## 📁 Repository Contents

* `src/` — Core modules (API client, trading logic, configuration)
* `logs/` — Execution logs for MARKET and LIMIT orders
* `main.py` — Entry point for the Typer CLI application
* `requirements.txt` — Python dependencies
* `.env.example` — Template for required environment variables
* `.gitignore` — Git ignore rules to protect API keys

## 🔐 Environment Setup

**1. Clone the repository and navigate to the project directory:**

    git clone https://github.com/YARAGANIDURGADHANUSH/binance-trading-bot.git
    cd binance-trading-bot

**2. Install the required dependencies:**

    pip install -r requirements.txt

**3. Configure your API Keys:**
Create a `.env` file in the root directory and add your Binance Testnet credentials:

    BINANCE_API_KEY=your_testnet_api_key_here
    BINANCE_API_SECRET=your_testnet_secret_key_here

## 🛠️ Usage Instructions

The bot is operated entirely via the command line. Use the following commands to interact with the testnet:

**Check Account Balance:**

    python main.py balance

**Place a Market Order (e.g., Buy 0.001 BTC):**

    python main.py trade --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

**Place a Limit Order (e.g., Sell 0.001 BTC at $65,000):**

    python main.py trade --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000

## 👨‍💻 Author

Durga Dhanush Yaragani
