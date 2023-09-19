import hashlib
import ecdsa
from PIL import Image
from stegan import Encode, Decode
import math
global signature
import cv2
def Encrypt1(original_image_file):
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    print("ENTER THE TEXT::::")
    inpt=input()
    # Encode a message to be encrypted
    message = inpt.encode()

    # Create a SHA-256 hash of the message
    message_hash = hashlib.sha256(message).digest()

    # Sign the hash using the private key
    signature = private_key.sign(message_hash)

    # Verify the signature using the public key
    assert public_key.verify(signature, message_hash)
    hexcode=signature.hex()
    # Output the encrypted message and signature
    print("Encrypted message:", message)
    print("Signature:", signature.hex())
    X=[]
    for i in range(len(signature)):
        X.append(signature[i])
    # encrypts a plaintext message using the current key
    img = Image.open(original_image_file)
    #print(img, img.mode)
    encoded_image_file = "enc_" + original_image_file
    img_encoded = Encode(img, signature, X)
    img_encoded.save("sign.png")
    return hexcode
    #print(img_encoded)
    # if img_encoded:
    #     img_encoded.save(encoded_image_file)
    #     print("{} saved!".format(encoded_image_file))




