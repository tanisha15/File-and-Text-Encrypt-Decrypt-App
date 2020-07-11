from Crypto import Random
from Crypto.Cipher import AES
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *

#the key to encrypt or decrypt symmetrically with
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'

#adding the padding or extra characters to make the string an eligible block size
def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)  # pad the string to the correct block size
    iv = Random.new().read(AES.block_size)  # initialization vector to prevent repitition in encryption
    cipher = AES.new(key, AES.MODE_CBC, iv)  # create the actual cipher object to encrypt with
    return iv + cipher.encrypt(message)  # return the full cipher text version of the string

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]#initialization vector for the first part of the ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv) #get a cipher text to encrypt/decrypt with
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])#decrypt the ciphertext
    return plaintext.rstrip(b"\0")#take out the padded characters to get the original string



#encrypt a file
def encrypt_file(file_name,key):
    with open(file_name, 'rb') as fo:#open file read it as a binary
        plaintext = fo.read()#store the text from the file
    enc = encrypt(plaintext,key)#encrypt the text
    with open(file_name + ".enc", 'wb') as fo:#create a new file with .enc extension and write as binary
        fo.write(enc) #write or place the encrypted cipher text in the new file

#decrypt a file
def decrypt_file(file_name,key):
    with open(file_name, 'rb') as fo:#open the file reading as binary
        ciphertext = fo.read()# store the ciphertext from the file
    dec = decrypt(ciphertext, key) #store the decrypted text in variable dec
    with open(file_name[:-4], 'wb') as fo:# open the original text file writing as binary
        fo.write(dec)#write the decrypted text in the text file

filename=None

#get the text file from the user
def load_text_file():
    global key, filename#global variables
    text_file=tk.filedialog.askopenfile(filetypes=[('Text Files','txt')])#get the file address
    if text_file.name!=None:#if a file was selected
        filename=text_file.name# set the global variable to the selected file's name

#encrypt the function for the GUI button
def encrypt_the_file():
    global key, filename
    if filename!= None:#encrypt the file
        encrypt_file(filename,key)
    else:#show error
        messagebox.showerror(title="Error:", message="There was no file loaded to encrypt")

#decrypt the file for the GUI button
def decrypt_the_file():
    global key, filename
    if filename != None:#decrypt the file
        fname= filename+ '.enc'
        decrypt_file(fname,key)
    else:#show error
        messagebox.showerror(title="Error:", message="There was no file loaded to encrypt")


#create the GUI window
root=tk.Tk()
root.title("File-Encryption-Decryption-App")
pic = PhotoImage(file = "lock.png")
root.iconphoto(False,pic)
root.minsize(width=500,height=80)
root.maxsize(width=500,height=80)


#loading the buttons
loadButton=tk.Button(root,text="Load Your Text File To Secure It", command=load_text_file)
encryptButton=tk.Button(root,text="Encrypt The File To Protect It", command=encrypt_the_file)
decryptButton=tk.Button(root,text="Decrypt The File To Retrieve It", command=decrypt_the_file)

#attaching the buttons
loadButton.pack()
encryptButton.pack()
decryptButton.pack()

root.mainloop()
















