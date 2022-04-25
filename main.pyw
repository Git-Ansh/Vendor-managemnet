import database
from tkinter import messagebox
import Vendor as v
from Cryptodome.Cipher import PKCS1_OAEP
import Driver as d
f=open("crclstp.txt","r+")
l=f.readlines(0)
def decryption():
    o = l[0]
    if o == 'faksnccfhslkfctag':
        d.rolecheck()
    elif o == 'ctagakjdkasdnal':
        v.login()
    else:
        messagebox.showerror("Tampering", "tampering")
if l==[]:
    v.login()
else:
    decryption()