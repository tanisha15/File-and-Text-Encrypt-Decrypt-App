import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()#creating a window

pic = PhotoImage(file = "lock.png")# For changing the icon of the title bar
root.iconphoto(False,pic)
root.title("Text Encryptor-Decryptor")#Title for the window

root.geometry("400x500")#size for the window
root.resizable(width=FALSE, height=FALSE)

canvas = tk.Canvas(root,height = 500, width=400, bg="MediumPurple1")#creating a canvas of same size of purple colour
canvas.pack()#attaching it to the window

bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")#changing the font of the text

label1 = tk.Label(root,text= "Enter the Text",width=20,bg="MediumPurple1")#creating a label which the user can view
label1.config(font=bold_font)
canvas.create_window(200,100,window=label1)
user_text = tk.Entry(root)#creating a box for the user to enter text
canvas.create_window(200,150,window=user_text)#attaching it to the canvas

label2=tk.Label(root,text="Choose an Operation",width=25,bg="MediumPurple1")#2nd operation for label2 in the same way
label2.config(font=bold_font)
canvas.create_window(200,200,window=label2)

v = tk.IntVar()#declaring tkinter variable

def choice():#depends upon the choice of user
    x = v.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()

#creating the radiobuttons for the encryption and decryption operation
label3=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="light yellow")
label3.config(font=bold_font)
canvas.create_window(100,250,window=label3)
label4=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="light yellow")
label4.config(font=bold_font)
canvas.create_window(300,250,window=label4)

def encryption():
    plain_text = user_text.get()#getting the user text and storing it in this variable
    cipher_text = ""#to store the result
    key = 3# for caeser cipher key value is 3
    for i in range(len(plain_text)):#traversing the text
        letter = plain_text[i]
        if(letter.isupper()):
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
            cipher_text+=chr((ord(letter)+key-97)%26+97)
    label5 =tk.Label(root,text=cipher_text,width=20,bg="light yellow")#creating a label with a text and attaching it to the root
    label5.config(font=bold_font)#changing the font
    canvas.create_window(200,350,window=label5)

def decryption():
    cipher_text = user_text.get()
    plain_text = ""
    key = 3
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
            plain_text+=chr((ord(letter)-key-97)%26+97)
    label6 =tk.Label(root,text=plain_text,width=20,bg="light yellow")
    label6.config(font=bold_font)
    canvas.create_window(200,350,window=label6)

label7 =tk.Label(root,text="Converted Text ",width=20,bg="MediumPurple1")#creating label for the converted text
label7.config(font=bold_font)
canvas.create_window(200,300,window=label7)#attaching it to the canvas

root.mainloop()