# SPDX-License-Identifier: MIT
# Coded Dua - "The Key Is With Him"
# A symbolic prayer in code to remind us that the unseen keys belong to Allahﷻ

import secrets
import hashlib
import ecdsa
from eth_utils import keccak, to_checksum_address


def generate_eth_keypair():
    # Generate a 256-bit private key randomly
    private_key = secrets.token_bytes(32)

    # Use ECDSA to derive the public key
    signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.verifying_key

    # Format public key properly
    public_key = verifying_key.to_string("uncompressed")

    # Derive Ethereum address from public key
    pub_key_keccak = keccak(public_key)
    eth_address = "0x" + pub_key_keccak[-20:].hex()

    return {
        "private_key_hex": private_key.hex(),
        "public_key_hex": public_key.hex(),
        "address": to_checksum_address(eth_address)
    }


def check_for_dead_address(target="0x000000000000000000000000000000000000dEaD"):
    attempts = 0

    print("🕌 Starting the search...")
    print("⏳ This is not a brute-force — it is a meditation.")
    print("📿 Each attempt is a reminder: 'The keys of the unseen are with Allah.'\n")

    while True:
        attempts += 1
        keys = generate_eth_keypair()

        if keys["address"].lower() == target.lower():
            print("\n✨ Found matching keypair (by destiny, not chance):")
            print(f"Private Key: {keys['private_key_hex']}")
            print(f"Public Key : {keys['public_key_hex']}")
            print(f"Address    : {keys['address']}")
            print(f"\n🔁 Attempts: {attempts}")
            print("\n📜 This was not found by you — it was revealed by Him.")
            break

        if attempts % 100 == 0:
            print(f"[Attempt #{attempts}] Still searching... Remember: 'All things are with Allah.'")


if __name__ == "__main__":
    check_for_dead_address()