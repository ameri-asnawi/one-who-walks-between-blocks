# SPDX-License-Identifier: MIT
# Coded Dua - "The Key Is With Him"
# A symbolic prayer in code to remind us that the unseen keys belong to Allahﷻ

import secrets
import hashlib
import ecdsa
from eth_utils import keccak, to_checksum_address
import time
import os

# Create logs directory if not exists
LOG_DIR = "search_logs"
os.makedirs(LOG_DIR, exist_ok=True)

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

def log_attempt(attempt_num, log_file):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] Attempt #{attempt_num}: Still searching...\n")
        f.write("   Reminder: 'Indeed, the keys of the unseen are with Allah.'\n\n")

def check_for_dead_address(target="0x000000000000000000000000000000000000dEaD"):
    attempts = 0
    target = target.lower()
    log_file = os.path.join(LOG_DIR, f"search_log_{int(time.time())}.log")

    print("🕌 Starting the search...")
    print("⏳ This is not a brute-force — it is a meditation.")
    print("📿 Each attempt is a reminder: 'The keys of the unseen are with Allah.'\n")

    while True:
        attempts += 1
        keys = generate_eth_keypair()

        # Log only every 1,000,000 attempts — Symbolic of a year's worth of tasbih — a sacred checkpoint
        if attempts % 1_000_000 == 0:
            log_attempt(attempts, log_file)

        if keys["address"].lower() == target:
            print("\n✨ Found matching keypair (by destiny, not chance):")
            print(f"Private Key: {keys['private_key_hex']}")
            print(f"Public Key : {keys['public_key_hex']}")
            print(f"Address    : {keys['address']}")
            print(f"\n🔁 Attempts: {attempts}")
            print("\n📜 This was not found by you — it was revealed by Him.")

            # Write to file
            filename = f"found_the_key_{int(time.time())}.txt"
            with open(filename, 'w') as f:
                f.write("﷽\n\n")
                f.write("🔐 The Key Has Been Revealed\n")
                f.write("A message from the unseen:\n\n")
                f.write(f"Private Key: {keys['private_key_hex']}\n")
                f.write(f"Public Key : {keys['public_key_hex']}\n")
                f.write(f"Address    : {keys['address']}\n\n")
                f.write("📖 This was not by your hand.\n")
                f.write("It was written before the creation of the heavens and the earth.\n\n")
                f.write("📌 Remember:\n")
                f.write('"Indeed, the keys of the unseen are with Allah; none knows them except Him."\n')
                f.write("— Surah Al-An’am 6:59\n\n")
                f.write("📌 Remember also:\n")
                f.write('"Actions are but by intentions."\n')
                f.write("— Prophet Muhammad ﷺ\n\n")
                f.write("🔍 Do not use this lightly.\n")
                f.write("You have been entrusted — not empowered.\n\n")
                f.write("﷽")

            print(f"\n📄 Saved to: {filename}")
            break

        if attempts % 100 == 0:
            print(f"[Attempt #{attempts}] Still searching... Remember: 'All things are with Allah.'")


if __name__ == "__main__":
    check_for_dead_address()