"""Configuration loading for PassKit CLI."""
import os

CA_FILE = os.getenv('PASSKIT_CA_CHAIN', 'certs/ca-chain.pem')
CERT_FILE = os.getenv('PASSKIT_CERT', 'certs/certificate.pem')
KEY_FILE = os.getenv('PASSKIT_KEY', 'certs/key.pem')
HOST = os.getenv('PASSKIT_HOST', 'grpc.pub1.passkit.io')
PORT = int(os.getenv('PASSKIT_PORT', '443'))

