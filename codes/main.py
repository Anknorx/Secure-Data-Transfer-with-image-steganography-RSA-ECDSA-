from tkinter import *
from tkinter import filedialog
from LSB_Technique import *
from PIL import ImageTk, Image
from rsa import *
from ecc import *

root = Tk()
root.title("Cryptography Tool")

def lsb_technique():
    option_window = Toplevel(root)
    option_window.title("LSB Technique")
    option_window.geometry("400x300")
    
    def encrypt():
        plain_image = filedialog.askopenfilename(title="Select Plain Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        cipher_image = filedialog.asksaveasfilename(title="Save Encoded Image As", filetypes=[("PNG Files", "*.png")], defaultextension=".png")
        code_message = code_message_entry.get()
        encoded_image = encode(image_name=plain_image, code_message=code_message)
        cv2.imwrite(cipher_image, encoded_image)
        status_label.config(text="Image encrypted successfully!")
    
    def decrypt():
        cipher_image = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG Files", "*.png")])
        decoded_data = decode(cipher_image)
        result_window = Toplevel(option_window)
        result_window.title("Decoded Data")
        result_window.geometry("400x300")
        result_label = Label(result_window, text=decoded_data, font=("Arial", 12))
        result_label.pack(pady=20)
    
    option_label = Label(option_window, text="Choose an option", font=("Arial", 16))
    option_label.pack(pady=20)
    
    encrypt_button = Button(option_window, text="Encrypt", font=("Arial", 12), command=encrypt)
    encrypt_button.pack(pady=10)
    
    decrypt_button = Button(option_window, text="Decrypt", font=("Arial", 12), command=decrypt)
    decrypt_button.pack(pady=10)
    
    code_message_label = Label(option_window, text="Enter Secret Message", font=("Arial", 12))
    code_message_label.pack(pady=10)
    
    code_message_entry = Entry(option_window, font=("Arial", 12))
    code_message_entry.pack(pady=10)
    
    back_button = Button(option_window, text="Back", font=("Arial", 12), command=option_window.destroy)
    back_button.pack(pady=20)
    
    status_label = Label(option_window, text="", font=("Arial", 12))
    status_label.pack(pady=20)
    

def lsb_using_rsa():
    option_window = Toplevel(root)
    option_window.title("LSB Using RSA Technique")
    option_window.geometry("400x300")
    
    def encrypt():
        plain_image = filedialog.askopenfilename(title="Select Plain Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        cipher_image = filedialog.asksaveasfilename(title="Save Encoded Image As", filetypes=[("PNG Files", "*.png")], defaultextension=".png")
        code_message = code_message_entry.get()
        encoded_image = encode(image_name=plain_image, code_message=code_message)
        cv2.imwrite(cipher_image, encoded_image)
        status_label.config(text="Image encrypted successfully!")
    
    def decrypt():
        cipher_image = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG Files", "*.png")])
        decoded_data = decode(cipher_image)
        result_window = Toplevel(option_window)
        result_window.title("Decoded Data")
        result_window.geometry("400x300")
        result_label = Label(result_window, text=decoded_data, font=("Arial", 12))
        result_label.pack(pady=20)

    option_label = Label(option_window, text="Choose an option", font=("Arial", 16))
    option_label.pack(pady=20)
    
    encrypt_button = Button(option_window, text="Encrypt", font=("Arial", 12), command=encrypt)
    encrypt_button.pack(pady=10)
    
    decrypt_button = Button(option_window, text="Decrypt", font=("Arial", 12), command=decrypt)
    decrypt_button.pack(pady=10)
    
    code_message_label = Label(option_window, text="Enter Secret Message", font=("Arial", 12))
    code_message_label.pack(pady=10)
    
    code_message_entry = Entry(option_window, font=("Arial", 12))
    code_message_entry.pack(pady=10)
    
    back_button = Button(option_window, text="Back", font=("Arial", 12), command=option_window.destroy)
    back_button.pack(pady=20)
    
    status_label = Label(option_window, text="", font=("Arial", 12))
    status_label.pack(pady=20)
        
def lsb_using_ecc():
    option_window = Toplevel(root)
    option_window.title("LSB Using ECC Technique")
    option_window.geometry("400x300")
    
    def encrypt():
        image = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        inp=Encrypt1(image)
      
        cipher_image = "enc_" + image
        encode(image, cipher_image)
        status_label.config(text=inp)
        # status_label.config(text="Image encrypted successfully!")
    
    def decrypt():
        cipher_image = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG Files", "*.png")])
        decoded_data = decode(cipher_image)
        result_window = Toplevel(option_window)
        result_window.title("Decoded Data")
        result_window.geometry("400x300")
        result_label = Label(result_window, text=decoded_data, font=("Arial", 12))
        result_label.pack(pady=20)
    
    option_label = Label(option_window, text="Choose an option", font=("Arial", 16))
    option_label.pack(pady=20)
    
    encrypt_button = Button(option_window, text="Encrypt", font=("Arial", 12), command=encrypt)
    encrypt_button.pack(pady=10)
    
    
    back_button = Button(option_window, text="Back", font=("Arial", 12), command=option_window.destroy)
    back_button.pack(pady=20)
    
    status_label = Label(option_window, text="", font=("Arial", 12))
    status_label.pack(pady=20)


lsb_button = Button(root, text="LSB Technique", font=("Arial", 14), command=lsb_technique)
lsb_button.pack(pady=20)

lsb_rsa_button = Button(root, text="LSB Using RSA Technique", font=("Arial", 14), command=lsb_using_rsa)
lsb_rsa_button.pack(pady=20)

lsb_ecc_button = Button(root, text="LSB Using ECC Technique", font=("Arial", 14), command=lsb_using_ecc)
lsb_ecc_button.pack(pady=20)

root.mainloop()
    