# https://bitcoinlib.readthedocs.io/en/latest/#multi-signature-wallets

from typing import cast
from bitcoinlib.wallets import Wallet, WalletError, wallet_delete_if_exists
from bitcoinlib.keys import HDKey
import random

# Create a Multisig wallet with 2 cosigners which both need to sign a transaction.

NETWORK = 'testnet'
k1 = HDKey('tprv8ZgxMBicQKsPd1Q44tfDiZC98iYouKRC2CzjT3HGt1yYw2zuX2awTotzGAZQEAU9bi2M5MCj8iedP9MREPjUgpDEBwBgGi2C8eK'
           '5zNYeiX8', network=NETWORK)
k2 = HDKey('tprv8ZgxMBicQKsPeUbMS6kswJc11zgVEXUnUZuGo3bF6bBrAg1ieFfUdPc9UHqbD5HcXizThrcKike1c4z6xHrz6MWGwy8L6YKVbgJ'
           'MeQHdWDp', network=NETWORK)

print(k1.address())

r = random.randint(1, 1145141919810)

wallet_delete_if_exists('multisig_2of2_cosigner1')
wallet_delete_if_exists('multisig_2of2_cosigner2')

w1 = Wallet.create('multisig_2of2_cosigner1', sigs_required=2,
                    keys=[k1, k2.public_master(multisig=True)], network=NETWORK)

w2 = Wallet.create('multisig_2of2_cosigner2',  sigs_required=2,
                    keys=[k1.public_master(multisig=True), k2], network=NETWORK)


w1 = cast(Wallet, w1)
w2 = cast(Wallet, w2)

print(w1.get_key())
print(w2.get_key())

# An address starting with "2": a testnet p2sh address
print("Deposit testnet bitcoin to this address to create transaction: ", w1.get_key().address)
# Create a transaction in the first wallet

w1.utxos_update()
# send from UTXO to 'mwCwTceJvYV27KXBc3NJZys6CjsgsoeHmf'
# SHOULD send but there is not enough fee
t = w1.sweep('mwCwTceJvYV27KXBc3NJZys6CjsgsoeHmf', min_confirms=0)
t.info()

# And then import the transaction in the second wallet, sign it and push it to the network

# w2.get_key()
t2 = w2.transaction_import(t)
t2.sign()

t2.send() # SHOULD send, but there is not enough fee
t2.info()
