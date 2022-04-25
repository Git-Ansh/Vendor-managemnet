import database
import threading
import tkinter as t
from tkinter import ttk
from tkinter import messagebox
from time import strftime
import Vendor as v
c=database.c
f=open("usr.txt", "r+")
o=f.readlines()
def add_product():
    rot = t.Tk()
    rot.title(f'Inventory for {o[0]}')
    rot.geometry('1920x1080')
    canvas = t.Canvas(rot, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)

    menubar = t.Menu(rot)
    nav = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Navigation', menu=nav)
    nav.add_command(label='Back to Dashboard', command=lambda: [rot.destroy(), vendorhome()])
    nav.add_separator()
    nav.add_command(label='Exit', command=lambda: [rot.destroy()])

    acc = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Account', menu=acc)
    acc.add_command(label='Log Out', command=logout)
    acc.add_command(label='Log Out & Exit', command=lambda: [logout(), rot.destroy()])
    acc.add_separator()
    acc.add_command(label='Exit', command=rot.destroy)

    def time():
        string = strftime('%A, %b %d, %H:%M:%S %p, %Y')
        labl.config(text=string)
        labl.after(1000, time)

    labl = t.Label(rot, font=('calibri', 15), bg='black', foreground='white')
    labl.pack()
    time()
    canvas.create_window(960, 95, window=labl)
  #  filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
  #  canvas.create_image(0, 0, image=filename, anchor="nw")
    canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
    canvas.create_text(960, 130, text=f"Welcome to your inventory, {o[0]} ", fill="white",
                       font=("courier", 20, "italic"))
    canvas.create_text(75, 20, text=f"Logged-in as {o[0]}", fill="white", font=("courier", 10, "italic"))

    style = ttk.Style(rot)
    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="black", foreground="turquoise")
    columns = ('pid', 'p_name', 'p_qty', 'p_dsc', 'p_prc', 'emi')
    tree = ttk.Treeview(rot, columns=columns, show='headings', height=39)
    tree.heading('pid', text='pid')
    tree.heading('p_name', text='p_name')
    tree.heading('p_qty', text='p_qty')
    tree.heading('p_dsc', text='p_dsc')
    tree.heading('p_prc', text='p_prc')
    tree.heading('emi', text='emi')
    s = []
    id = []
    nm = []
    qt = []
    ds = []
    prc = []
    emi = []
    c.execute("select product_id from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        id.append(uip)
    c.execute("select product_qty from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        qt.append(uip)
    c.execute("select product_name from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        nm.append(uip)
    c.execute("select product_description from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ds.append(uip)
    c.execute("select product_price from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        prc.append(uip)
    c.execute("select emi_available from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        emi.append(uip)
    c.execute("select product_id from items where vendor_id='" + o[0] + "'")
    k = 0
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ui = int(uip)
        s.append(ui)
    for i in s:
        k += 1
    print(k)
    for i in range(0, k):
        tree.insert('', t.END, values=(id[i], nm[i], qt[i], ds[i], prc[i], emi[i]))
    canvas.create_window(1301, 580, window=tree)
    scrollbar = ttk.Scrollbar(rot, orient=t.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    canvas.create_window(1910, 300, window=scrollbar)

    opt = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Options', menu=opt)
    opt.add_command(label='Add Product', command=lambda: [rot.destroy()])
    opt.add_command(label='Delete Product', command=lambda: [])
    rot.config(menu=menubar)
    rot.mainloop()
def delete_product():
    rot = t.Tk()
    rot.title(f'Inventory for {o[0]}')
    rot.geometry('1920x1080')
    canvas = t.Canvas(rot, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)

    menubar = t.Menu(rot)
    nav = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Navigation', menu=nav)
    nav.add_command(label='Back to Dashboard', command=lambda: [rot.destroy(), vendorhome()])
    nav.add_separator()
    nav.add_command(label='Exit', command=lambda: [rot.destroy()])

    acc = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Account', menu=acc)
    acc.add_command(label='Log Out', command=logout)
    acc.add_command(label='Log Out & Exit', command=lambda: [logout(), rot.destroy()])
    acc.add_separator()
    acc.add_command(label='Exit', command=rot.destroy)

    def time():
        string = strftime('%A, %b %d, %H:%M:%S %p, %Y')
        labl.config(text=string)
        labl.after(1000, time)

    labl = t.Label(rot, font=('calibri', 15), bg='black', foreground='white')
    labl.pack()
    time()
    canvas.create_window(960, 95, window=labl)
 #   filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
   # canvas.create_image(0, 0, image=filename, anchor="nw")
    canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
    canvas.create_text(960, 130, text=f"Welcome to your inventory, {o[0]} ", fill="white",
                       font=("courier", 20, "italic"))
    canvas.create_text(75, 20, text=f"Logged-in as {o[0]}", fill="white", font=("courier", 10, "italic"))

    style = ttk.Style(rot)
    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="black", foreground="turquoise")
    columns = ('pid', 'p_name', 'p_qty', 'p_dsc', 'p_prc', 'emi')
    tree = ttk.Treeview(rot, columns=columns, show='headings', height=39)
    tree.heading('pid', text='pid')
    tree.heading('p_name', text='p_name')
    tree.heading('p_qty', text='p_qty')
    tree.heading('p_dsc', text='p_dsc')
    tree.heading('p_prc', text='p_prc')
    tree.heading('emi', text='emi')
    s = []
    id = []
    nm = []
    qt = []
    ds = []
    prc = []
    emi = []
    c.execute("select product_id from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        id.append(uip)
    c.execute("select product_qty from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        qt.append(uip)
    c.execute("select product_name from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        nm.append(uip)
    c.execute("select product_description from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ds.append(uip)
    c.execute("select product_price from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        prc.append(uip)
    c.execute("select emi_available from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        emi.append(uip)
    c.execute("select product_id from items where vendor_id='" + o[0] + "'")
    k = 0
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ui = int(uip)
        s.append(ui)
    for i in s:
        k += 1
    print(k)
    for i in range(0, k):
        tree.insert('', t.END, values=(id[i], nm[i], qt[i], ds[i], prc[i], emi[i]))
    canvas.create_window(1301, 580, window=tree)
    scrollbar = ttk.Scrollbar(rot, orient=t.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    canvas.create_window(1910, 300, window=scrollbar)

    opt = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Options', menu=opt)
    opt.add_command(label='Add Product', command=lambda: [rot.destroy()])
    opt.add_command(label='Delete Product', command=lambda: [])
    rot.config(menu=menubar)
    rot.mainloop()
def update_product():
    rot = t.Tk()
    rot.title(f'Inventory for {o[0]}')
    rot.geometry('1920x1080')
    canvas = t.Canvas(rot, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)

    menubar = t.Menu(rot)
    nav = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Navigation', menu=nav)
    nav.add_command(label='Back to Dashboard', command=lambda: [rot.destroy(), vendorhome()])
    nav.add_separator()
    nav.add_command(label='Exit', command=lambda: [rot.destroy()])

    acc = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Account', menu=acc)
    acc.add_command(label='Log Out', command=logout)
    acc.add_command(label='Log Out & Exit', command=lambda: [logout(), rot.destroy()])
    acc.add_separator()
    acc.add_command(label='Exit', command=rot.destroy)

    def time():
        string = strftime('%A, %b %d, %H:%M:%S %p, %Y')
        labl.config(text=string)
        labl.after(1000, time)

    labl = t.Label(rot, font=('calibri', 15), bg='black', foreground='white')
    labl.pack()
    time()
    canvas.create_window(960, 95, window=labl)
 #   filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
  #  canvas.create_image(0, 0, image=filename, anchor="nw")
    canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
    canvas.create_text(960, 130, text=f"Welcome to your inventory, {o[0]} ", fill="white",
                       font=("courier", 20, "italic"))
    canvas.create_text(75, 20, text=f"Logged-in as {o[0]}", fill="white", font=("courier", 10, "italic"))

    style = ttk.Style(rot)
    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="black", foreground="turquoise")
    columns = ('pid', 'p_name', 'p_qty', 'p_dsc', 'p_prc', 'emi')
    tree = ttk.Treeview(rot, columns=columns, show='headings', height=39)
    tree.heading('pid', text='pid')
    tree.heading('p_name', text='p_name')
    tree.heading('p_qty', text='p_qty')
    tree.heading('p_dsc', text='p_dsc')
    tree.heading('p_prc', text='p_prc')
    tree.heading('emi', text='emi')
    s = []
    id = []
    nm = []
    qt = []
    ds = []
    prc = []
    emi = []
    c.execute("select product_id from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        id.append(uip)
    c.execute("select product_qty from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        qt.append(uip)
    c.execute("select product_name from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        nm.append(uip)
    c.execute("select product_description from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ds.append(uip)
    c.execute("select product_price from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        prc.append(uip)
    c.execute("select emi_available from items where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        emi.append(uip)
    c.execute("select product_id from items where vendor_id='" + o[0] + "'")
    k = 0
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ui = int(uip)
        s.append(ui)
    for i in s:
        k += 1
    print(k)
    for i in range(0, k):
        tree.insert('', t.END, values=(id[i], nm[i], qt[i], ds[i], prc[i], emi[i]))
    canvas.create_window(1301, 580, window=tree)
    scrollbar = ttk.Scrollbar(rot, orient=t.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    canvas.create_window(1910, 300, window=scrollbar)

    opt = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Options', menu=opt)
    opt.add_command(label='Add Product', command=lambda: [rot.destroy()])
    opt.add_command(label='Delete Product', command=lambda: [])
    rot.config(menu=menubar)
    rot.mainloop()