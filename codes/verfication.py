import hashlib
import ecdsa
from PIL import Image
from stegan import Encode, Decode
import math
import cv2
from verify1 import *
from ecc import *
# print("Signature :",hexcode)

hexcode=veri()
print("ENTER THE RECIEVED HASH ::::")
inpt2=input()

if(inpt2==hexcode):
    print("Verified")
else:
    print("Image was tampered")

