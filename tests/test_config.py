import os
from passkit_cli import config

def test_defaults():
    assert config.CA_FILE.endswith('ca-chain.pem')
    assert config.HOST

