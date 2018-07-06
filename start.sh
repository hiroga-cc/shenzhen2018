# Set environment variables
. ./env

# Run bitcoin wallet
blockchain-wallet-service start --port 3000 &

# Run QR Code Reader
python -B src/start_qrcode_reader.py &

# Run Garbage Recognition

