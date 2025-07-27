# Trading Bot - Binance Futures Trading Bot

A simple Python trading bot for Binance Futures that allows you to place market and limit orders through an interactive command-line interface.

## Features

- **Binance Futures Integration**: Connect to Binance Futures API (supports testnet)
- **Order Types**: Support for MARKET and LIMIT orders
- **Buy/Sell Orders**: Place both BUY and SELL orders
- **Interactive CLI**: User-friendly command-line interface
- **Logging**: Comprehensive logging of all operations
- **Error Handling**: Robust error handling with detailed error messages

## Prerequisites

- Python 3.7 or higher
- Binance account with Futures trading enabled
- API key and secret from Binance

## Installation

### Step 1: Clone or Download the Bot

Download all files to your local directory:

- `main.py`
- `bot.py`
- `requirements.txt`
- `Readme.md`

### Step 2: Install Dependencies

Open a terminal/command prompt in the bot directory and run:

```bash
pip install -r requirements.txt
```

This will install:

- `python-binance`: Official Binance Python API connector
- `python-dotenv`: For environment variable management

### Step 3: Set Up API Credentials

#### Option A: Direct Configuration (Current Setup)

The bot currently has API credentials hardcoded in `main.py`. These appear to be testnet credentials.

#### Option B: Environment Variables (Recommended)

1. Create a `.env` file in the bot directory:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

2. Update `main.py` to use environment variables:

```python
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
```

## Getting Your Binance API Keys

1. Log in to your Binance account
2. Go to Account → API Management
3. Create a new API key
4. **Important**: Enable "Enable Futures" permission
5. Copy your API Key and Secret Key
6. **Security**: Restrict API access to your IP address

## Usage

### Step 1: Run the Bot

```bash
python main.py
```

### Step 2: Follow the Interactive Prompts

The bot will ask you for the following information:

1. **Symbol**: Enter the trading pair (e.g., `BTCUSDT`, `ETHUSDT`, `ADAUSDT`)

   - Use uppercase letters
   - Must be a valid Binance Futures symbol

2. **Side**: Choose order direction

   - `BUY`: Long position
   - `SELL`: Short position

3. **Order Type**: Choose order type

   - `MARKET`: Execute immediately at current market price
   - `LIMIT`: Execute only at specified price or better

4. **Quantity**: Enter the amount to trade

   - Must meet minimum quantity requirements for the symbol
   - Example: `0.001` for BTC, `1` for ADA

5. **Price** (for LIMIT orders only): Enter your desired price
   - Only required for LIMIT orders
   - Must be within price filters for the symbol

### Example Usage

```
Enter symbol (e.g., BTCUSDT): BTCUSDT
Enter side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): LIMIT
Enter quantity: 0.001
Enter limit price: 45000

Placing LIMIT BUY order for BTCUSDT with qty=0.001, price=45000.0

Order placed successfully!
Order ID: 12345678
Status: NEW
```

## Testnet vs Live Trading

### Current Configuration

The bot is currently configured for **testnet** (paper trading):

```python
bot = BasicBot(api_key, api_secret, testnet=True)
```



## Monitoring and Logs

### Log File

All bot activities are logged to `log.txt`:

- Order placements
- API responses
- Errors and exceptions
- Timestamps for all activities

### Checking Logs

```bash
tail -f log.txt  # Real-time log monitoring
cat log.txt      # View entire log file
```

## Troubleshooting

### Common Issues

1. **Invalid Symbol Error**

   - Ensure symbol is available on Binance Futures
   - Use correct format (e.g., `BTCUSDT`, not `BTC/USDT`)

2. **Insufficient Balance**

   - Check your Futures wallet balance
   - Transfer funds from Spot to Futures wallet if needed

3. **API Permission Error**

   - Ensure "Enable Futures" is checked in API settings
   - Verify API key and secret are correct

4. **Price Filter Error**

   - Price doesn't meet symbol's price filter requirements
   - Check minimum/maximum price increments

5. **Quantity Filter Error**
   - Quantity is below minimum or above maximum
   - Check symbol's quantity filters

### Error Checking

1. Check `log.txt` for detailed error messages
2. Verify your API credentials
3. Ensure sufficient balance in Futures wallet
4. Confirm symbol is active and tradeable

## Safety Tips

### For Testnet

- Use testnet for learning and testing strategies
- Testnet uses fake money - no real trades

### For Live Trading

- **Start Small**: Test with minimal amounts first
- **Set Stop Losses**: Always have risk management
- **Monitor Positions**: Keep track of open positions
- **API Security**: Use IP restrictions and read-only when possible
- **Regular Review**: Check logs and trading performance

## File Structure

```
trading-bot/
├── main.py          # Main execution file
├── bot.py           # Bot class with trading logic
├── requirements.txt # Python dependencies
├── log.txt          # Log file (created automatically)
├── Readme.md        # This file
└── __pycache__/     # Python cache (auto-generated)
```



## Support

- Check `log.txt` for detailed error information
- Review Binance API documentation
- Ensure all dependencies are installed correctly


