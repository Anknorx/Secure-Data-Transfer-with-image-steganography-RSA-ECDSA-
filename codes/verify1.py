import hashlib
import ecdsa
from PIL import Image
from stegan import Encode, Decode
import math
import cv2
def veri():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    print("ENTER THE Recieved TEXT::::")
    inpt=input()
    # Encode a message to be encrypted
    message = inpt.encode()

    # Create a SHA-256 hash of the message
    message_hash = hashlib.sha256(message).digest()

    # Sign the hash using the private key
    signature = private_key.sign(message_hash)
    hexcode=signature.hex()

    # Verify the signature using the public key
    assert public_key.verify(signature, message_hash)
    return hexcode