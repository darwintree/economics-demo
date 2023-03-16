# demo

## library introduction

`python-bitoin-utils`: Library to interact with the Bitcoin network. Ideal for low-level learning and experimenting.
`bitcoinlib`: Bitcoin and other Cryptocurrencies Library for Python. Includes a fully functional wallet, Mnemonic key generation and management and connection with various service providers to receive and send blockchain and transaction information.

## dependency installation

### python-bitoin-utils

```bash
pip install bitcoin-utils
```

### bitcoinlib

The `bitcoinlib` requires [fastecdsa](https://fastecdsa.readthedocs.io/en/stable/installation.html), where extra dependencies are required.

```
pip install bitcoinlib
```

If installation failed, try below commands:

on MacOS

```
brew install gmp
env "CFLAGS=-I/usr/local/include -L/usr/local/lib" pip install bitcoinlib
```

## running

```bash
python 1and4-bitcoin-pk-sk.py # requires python-bitoin-utils
python 2-bitcoin-p2sh.py # requires python-bitoin-utils
python 2-bitcoin-multi.py # requires bitcoinlib
python 5-proof-of-work.py
```
