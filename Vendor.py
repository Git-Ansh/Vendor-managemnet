import Driver as dr
import database
import threading
import tkinter as t
from tkinter import ttk
from tkinter import messagebox
from time import strftime
import math
import smtplib
import random
import Products as p
c=database.c

#=========================================================NEW USER SIGN UP===========================================================================================================================================================================================================================================================================================================================================================
def signup():
    root = t.Tk()
    root.geometry("1920x1080")
    root.title("SIGN-UP")
    canvas = t.Canvas(root, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)
    name_var = t.StringVar()
    cpassw_var = t.StringVar()
    email_var = t.StringVar()
    passw_var = t.StringVar()
    vendnm_var=t.StringVar()
 #   filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
 #   canvas.create_image(0, 0, image=filename, anchor="nw")
    canvas.create_text(800,300, text='Your Name:', font=('courier', 18, 'bold'), fill='turquoise')
    canvas.create_text(830, 350, text='New Vendor ID:', font=('courier', 18, 'bold'), fill='turquoise')
    canvas.create_text(820, 400, text='New Password:', font=('courier', 18, 'bold'), fill='turquoise')
    canvas.create_text(845, 450, text='Confirm Password:', font=('courier', 18, 'bold'), fill='turquoise')
    canvas.create_text(805, 500, text='Your Email:', font=('courier', 18, 'bold'), fill='turquoise')
    canvas.create_text(825,550,text="Signing-up as:",font=('courier', 18, 'bold'), fill='turquoise' )
    name_entry = t.Entry(root, relief='groove', textvariable=name_var, bg='light blue', font=('courier', 15, 'normal'))
    passw_entry = t.Entry(root, relief='groove', textvariable=passw_var, bg='lightblue', font=('courier', 15, 'normal'),show='*')
    cpassw_entry = t.Entry(root, relief='groove', textvariable=cpassw_var, bg='light blue',font=('courier', 15, 'normal'), show='*')
    email_entry = t.Entry(root, relief='groove', textvariable=email_var, bg='light blue',font=('courier', 15, 'normal'))
    vennam_entry=t.Entry(root, relief='groove', textvariable=vendnm_var, bg='light blue', font=('courier', 15, 'normal'))
    clicked = t.StringVar()
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="light blue", background="white")
    clicked.set("Role")
    drop = ttk.Combobox(root,state="readonly",height=2,width=28, textvariable=clicked)
    drop['values'] = ["Vendor", "Client"]
    canvas.create_window(1090,300, window=vennam_entry)
    canvas.create_window(1090, 350, window=name_entry)
    canvas.create_window(1090, 400, window=passw_entry)
    canvas.create_window(1090, 450, window=cpassw_entry)
    canvas.create_window(1090, 500, window=email_entry)
    canvas.create_window(1090, 550, window=drop)
    def time():
        string = strftime('%A, %b %d, %H:%M:%S %p, %Y')
        labl.config(text=string)
        labl.after(1000, time)
    labl = t.Label(root, font=('calibri', 15),bg='black', foreground='white')
    labl.pack()
    time()
    canvas.create_window(960, 130, window=labl)
    canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
    def create():
        text = clicked.get()
        usrnm = name_var.get()
        password = passw_var.get()
        cp = cpassw_var.get()
        eml = email_var.get()
        vname=vendnm_var.get()
        if str(usrnm) != "" and str(password) != "" and str(eml) != "" and str(cp) != "":
            li = []
            em = []
            count = 0
            c.execute("select user_id from users")
            for i in c:
                ki = (str(i).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                li.append(ui)
            c.execute("select user_email from users")
            for i in c:
                mi = (str(i).strip('()').replace('\'', ''))
                ei = mi.strip(',').replace('\'', '  ')
                em.append(ei)
            if str(usrnm) in li:
                print("Username already exists")
                count += 1
                messagebox.showinfo("Prompt", "This ID already exists, Please try another one")
                # nop = t.Message(root, text='Username already exists',fg="red", font=('calibre', 10, 'bold'))
                # nop.grid(row=7, column=1)
            elif len(str(usrnm))>10:
                messagebox.showerror("Error", "user ID cannot be greater than 10 characters")
            elif str(cp) != str(password):
                messagebox.showerror("Error", "passwords do not match please reconfirm password")
                # nopelo = t.Message(root, text='passwords do not match please reconfirm password',font=('calibre', 10, 'bold'))
                # nopelo.grid(row=9, column=1)
            elif eml in em:
                messagebox.showerror("Error", "this email is already registered, please enter another one")
                print("this email is already registered, please enter another one")
                # nopel = t.Message(root, text='this email is already registered, please enter another one',fg="red",font=('calibre', 10, 'bold'))
                # nopel.grid(row=9, column=1)
            elif text=="Role":
                messagebox.showerror("Set Role", "Please Select A Valid Role")


            else:
                if text == "Vendor":
                    c.execute("insert into vendors (vendor_id,vendor_name,vendor_email) values('" + usrnm + "','" + vname + "','" + eml + "')")
                elif text == "Client":
                    c.execute("insert into customers (customer_id,customer_name,customer_email) values('" + usrnm + "','" + vname + "','" + eml + "')")
                cpr = str(password)
                c.execute("insert into users (user_id,user_email,password, role) values('" + usrnm + "','" + eml + "',AES_ENCRYPT('" + cpr + "','C-TAG'),'" + text + "')")
                root.destroy()
                login()
        else:
            messagebox.showinfo("Prompt", "PLEASE MAKE SURE NONE OF THE FIELDS ARE EMPTY")
            # no = t.Message(root, text='PLEASE MAKE SURE NONE OF THE FIELDS ARE EMPTY',fg="red", font=('calibre', 10, 'bold'))
            # no.grid(row=6, column=1)

    create_btn = t.Button(root, width=68, height=1, bg="turquoise", text='Create Account', command=create)
    login_btn = t.Button(root, width=31, height=1, bg="turquoise", text='Login',command=lambda: [root.destroy(), login()])
    cancel_btn = t.Button(root, width=31, height=1, bg="turquoise", text='Cancel',command=lambda: [root.destroy(), login()])
    canvas.create_window(975, 610, window=create_btn)
    canvas.create_window(844, 660, window=cancel_btn)
    canvas.create_window(1104, 660, window=login_btn)
    root.mainloop()
#=========================================================LOGIN=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
def login():
    root = t.Tk()
    root.geometry("1920x1080")
    root.title("LOGIN")
    canvas = t.Canvas(root, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)
    name_var = t.StringVar()
 #   filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
  #  canvas.create_image(0, 0, image=filename, anchor="nw")
    passw_var = t.StringVar()
    canvas.create_text(825, 400, text='User ID:', font=('courier', 18, 'bold'), fill='turquoise')
    name_entry = t.Entry(root, relief='sunken', textvariable=name_var, bg='light blue', font=('courier', 15, 'normal'))
    canvas.create_text(820, 450, text='Password:', font=('courier', 18, 'bold'), fill='turquoise')
    passw_entry = t.Entry(root, relief='sunken', textvariable=passw_var, bg='lightblue', font=('courier', 15, 'normal'),show='*')
    canvas.create_window(1020, 400, window=name_entry)
    canvas.create_window(1020, 450, window=passw_entry)
    def time():
        string = strftime('%A, %b %d, %H:%M:%S %p, %Y')
        labl.config(text=string)
        labl.after(1000, time)
    labl = t.Label(root, font=('calibri', 15),bg='black', foreground='white')
    labl.pack()
    time()
    canvas.create_window(960, 130, window=labl)
    canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))

    def rolecheck():
        root.destroy()
        f1 = open("usr.txt", "r+")
        oi = f1.readlines()
        c.execute("select role from users where user_id='" + oi[0] + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
        if uip == "Vendor":
            dr.vendorhome()
        elif uip == "Client":
            dr.customerhome()
    def submit():
        global uip
        username = name_var.get()
        o=open("usr.txt","a+")
        o.close()
        password = passw_var.get()
        if str(username) != "" and str(password) != "":
            li = []
            lik = []
            count = 0
            c.execute("select user_id from users")
            for i in c:
                ki = (str(i).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                li.append(ui)
            res = li
            c.execute("select cast(AES_DECRYPT(password,'C-TAG') as char) from users")
            for i in c:
                kik = (str(i).strip('()').replace('\'', ''))
                uik = kik.strip(',').replace('\'', '')
                lik.append(uik)
            resl = lik
            combined = zip(res, resl)
            valdict = {}
            for keys, value in combined:
                valdict[keys] = value
            if str(username) not in valdict:
                messagebox.showerror("Error", "This is not a valid username, input username again")
                # no=t.Message(root, text='This is not a valid username, input username again!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',fg="red", font=('calibre', 10, 'bold'))
                # no.grid(row=3,column=2)
                print("This is not a valid username, input username again!")
                count += 1
            else:
                pass
            if str(password) == valdict[str(username)]:
                f3 = open("usr.txt", "w+")
                f3.write(username)
                f3.close()
                f = open("crclstp.txt", "w")
                f.write('faksnccfhslkfctag')
                f.close()
                print("LOGIN SUCCESSFUL")
                rolecheck()


            elif str(username) in valdict and str(password) in valdict:
                pass
            elif str(password) != valdict[str(username)]:
                print("Password is not valid. ")
                messagebox.showerror("Error", "Password is Invalid")
                # no = t.Message(root, text='Password is not valid.',fg="red", font=('calibre', 10, 'bold'))
                # no.grid(row=4, column=2)
                count += 1
        else:
            messagebox.showinfo("Prompt", "PLEASE MAKE SURE NONE OF THE FIELDS ARE EMPTY")
            # no = t.Message(root, text='PLEASE MAKE SURE NONE OF THE FIELDS ARE EMPTY\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',fg="red", font=('calibre', 10, 'bold'))
            # no.grid(row=6, column=2)
#=====================================================================FORGOT PASSWORD========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

    def chk():
        username = name_var.get()
        if username != "":
            root.destroy()
            pass
        else:
            messagebox.showinfo("Empty Field", "Please Enter your Vendor ID to continue")
            root.destroy()
            login()
    def forgotpass():
        def sendotp():
            global OTP, emailid
            username = name_var.get()
            count = 0
            print("LOADING PLEASE WAIT...")
            em = []
            c.execute("select vendor_email from vendors where vendor_id='" + username + "'")
            for i in c:
                mi = (str(i).strip('()').replace('\'', ''))
                ei = mi.strip(',').replace('\'', '')
                em.append(ei)
            digits = "0123456789"
            OTP = ""
            for i in range(6):
                OTP += digits[math.floor(random.random() * 10)]
            otp = OTP + " is your Password Reset OTP."
            msg = otp
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("managerplus.client@gmail.com", "cpauwzvkkhybmjgf")
            emailid = em[0]
            s.sendmail('&&&&&&&&&&&', emailid, msg)
        rot=t.Tk()
        rot.geometry("1920x1080")
        rot.title("OTP VERIFICATION")
        can= t.Canvas(rot, width=1920, height=1080)
        can.pack(fill="both", expand=True)
     #   filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
     #   can.create_image(0, 0, image=filename, anchor="nw")
        otp_var = t.StringVar()
        can.create_text(960, 100, text="An OTP has been sent to the e-mail registered to Your Vendor ID.", fill="white", font=("courier", 15))
        na_entry = t.Entry(rot, relief='sunken', textvariable=otp_var, bg='light blue', font=('courier', 15, 'normal'))
        can.create_text(825, 420, text='Enter OTP:', font=('courier', 18, 'bold'), fill='turquoise')
        def verify():
            a = otp_var.get()
            if a==OTP:
                rot.destroy()
                ro = t.Tk()
                ro.geometry("1920x1080")
                ro.title("Password Reset")
                cant = t.Canvas(ro, width=1920, height=1080)
                cant.pack(fill="both", expand=True)
             #   filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
              #  cant.create_image(0, 0, image=filename, anchor="nw")
                e_var=t.StringVar()
                w_var=t.StringVar()
                cant.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
                cant.create_text(960, 100, text="Enter a new Password", fill="white", font=("courier", 15))
                cant.create_text(810, 400, text='New Password:', font=('courier', 18, 'bold'), fill='turquoise')
                ps_entry = t.Entry(ro, relief='sunken', textvariable=e_var, bg='light blue',font=('courier', 15, 'normal'), show='*')
                cant.create_text(782, 450, text='Confirm Password:', font=('courier', 18, 'bold'), fill='turquoise')
                conp_entry = t.Entry(ro, relief='sunken', textvariable=w_var, bg='light blue',font=('courier', 15, 'normal'), show='*')
                cp_btn = t.Button(ro, width=47, height=1, bg='turquoise', text='Reset Password',command=lambda: [resetpass()])
                cant.create_window(950, 510, window=cp_btn)
                cant.create_window(1020, 400, window=ps_entry)
                cant.create_window(1020, 450, window=conp_entry)
                def resetpass():
                    np = e_var.get()
                    cnp = w_var.get()
                    if np!=cnp:
                        messagebox.showerror("Password Missmatch","Passwords do not match, please enter them again.")
                    elif np==cnp:
                        print(cnp)
                        c.execute("update vendors set vendor_password=AES_ENCRYPT('" + cnp + "','C-TAG') where vendor_email='" + emailid + "'")
                        messagebox.showinfo("Reset Successful","Your password has been reset successfully.")
                        ro.destroy()
                        login()
                ro.mainloop()
            elif a!=OTP:
                messagebox.showerror("Incorrect OTP", "OTP Invalid")


        su_btn = t.Button(rot, width=47, height=1, bg='turquoise', text='Verify', command=lambda: [verify()])
        lbtn = t.Button(rot, width=47, height=1, bg='turquoise', text='Cancel',command=lambda: [rot.destroy(), login()])
        can.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
        can.create_window(950, 510, window=su_btn)
        can.create_window(950, 560, window=lbtn)
        can.create_window(1020, 420, window=na_entry)

        #messagebox.showinfo("OTP Sent", "An OTP has been sent to the email registered with your Vendor ID")
        def to():
            thread=threading.Thread(target=sendotp, args=())
            thread.daemon=True
            thread.start()
        to()
        rot.mainloop()
    sub_btn = t.Button(root, width=51, height=1, bg='turquoise', text='Login', command=lambda: [submit()])
    signin_btn = t.Button(root, width=22, height=1, bg='turquoise', text='Sign-Up',command=lambda: [root.destroy(), signup()])
    cancel_btn = t.Button(root, width=22, height=1, bg='turquoise', text='Forgot Password',command=lambda: [chk(),forgotpass()])
    canvas.create_window(955, 510, window=sub_btn)
    canvas.create_window(855, 560, window=cancel_btn)
    canvas.create_window(1055, 560, window=signin_btn)
    root.mainloop()
def logout():
    f1 = open("usr.txt", "w")
    f1.close()
    f = open("crclstp.txt", "w")
    f.write('ctagakjdkasdnal')
    f.close()
