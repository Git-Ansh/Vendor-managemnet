import database as d
import tkinter as t
from tkinter import messagebox
import Vendor as v
from time import strftime
import Products as p
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
c=d.c


def vendorhome():
    f = open("usr.txt", "r+")
    o = f.readlines()
    root = t.Tk()
    root.geometry("1920x1080")
    root.title(f"MANAGER+ - Vendor Dashboard | User - {o[0]}")
    canvas = t.Canvas(root, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)
    def time():
        string = strftime('%A, %b %d, %H:%M:%S %p, %Y')
        labl.config(text=string)
        labl.after(1000, time)
    labl = t.Label(root, font=('calibri', 15),bg='black', foreground='white')
    labl.pack()
    time()
    canvas.create_window(960, 95, window=labl)
#   filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
 #   canvas.create_image(0, 0, image=filename, anchor="nw")
    canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
    canvas.create_text(240, 180, text="-Vendor Dashboard-", fill="turquoise", font=("courier", 30, "italic"))
    canvas.create_text(320, 690, text="All Orders Linked To Your Vednor ID:", fill="turquoise", font=("courier", 20, "italic"))
    canvas.create_text(75, 20, text=f"Logged-in as {o[0]}", fill="white", font=("courier", 10, "italic"))
    canvas.create_text(960, 130, text=f"Welcome, {o[0]}", fill="white", font=("courier", 20, "italic"))
    def logout():
        f1 = open("usr.txt", "w")
        f1.close()
        f2 = open("usr.txt", "r+")
        op = f2.readlines()
        f = open("crclstp.txt", "w")
        f.write('ctagakjdkasdnal')
        f.close()
        root.destroy()
        v.login()
    def logoute():
        f1 = open("usr.txt", "w")
        f1.close()
        f = open("crclstp.txt", "w")
        f.write('ctagakjdkasdnal')
        f.close()
        root.destroy()
    def logout():
        f1 = open("usr.txt", "w")
        f1.close()
        f2 = open("usr.txt", "r+")
        op = f2.readlines()
        f = open("crclstp.txt", "w")
        f.write('ctagakjdkasdnal')
        f.close()
        root.destroy()
        v.login()
    def logoute():
        f1 = open("usr.txt", "w")
        f1.close()
        f = open("crclstp.txt", "w")
        f.write('ctagakjdkasdnal')
        f.close()
        root.destroy()
    menubar = t.Menu(root)
    acc = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Account', menu=acc)
    acc.add_command(label='Log Out', command=logout)
    acc.add_command(label='Log Out & Exit', command=logoute)
    acc.add_separator()
    acc.add_command(label='Exit', command=root.destroy)


    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview", background="black",fieldbackground="black", foreground="turquoise")
    columns = ('oid', 'p_name', 't_vlv', 'v_id', 'ord_qty', 'rwd_pt')
    tree = ttk.Treeview(root, columns=columns, show='headings',height=10)
    tree.heading('oid', text='Order ID')
    tree.heading('p_name', text='Product Name')
    tree.heading('t_vlv', text='Total Value')
    tree.heading('v_id', text='Vendor ID')
    tree.heading('ord_qty', text='Order Quantity')
    tree.heading('rwd_pt', text='Reward Points')
    s = []
    id = []
    nm = []
    qt = []
    ds = []
    prc = []
    emi = []
    c.execute("select order_id from orders where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        id.append(uip)
    c.execute("select product_name from orders where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        qt.append(uip)
    c.execute("select total_value from orders where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        nm.append(uip)
    c.execute("select vendor_id from orders where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ds.append(uip)
    c.execute("select order_quantity from orders where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        prc.append(uip)
    c.execute("select reward_point from orders where vendor_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        emi.append(uip)

    c.execute("select order_id from orders where vendor_id='" + o[0] + "'")
    k = 0
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ui = int(uip)
        s.append(ui)
    for i in s:
        k += 1
    for i in range(0, k):
        tree.insert('', t.END, values=(id[i], qt[i],nm[i] , ds[i], prc[i], emi[i]))
    scrollbar = ttk.Scrollbar(root, orient=t.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    def deletefrmtree():
        curItem = tree.focus()
        w=tree.item(curItem)['values']
        tree.delete(curItem)
        u=str(w[0])
        c.execute("delete from orders where order_id='"+u+"'")
    def appr():
        messagebox.showinfo("Order Approved","Order Approved and Queued for Dispatch")
    def rej():
        messagebox.showinfo("Order Denied","Order Request has been Denied")




    def inventory():
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
        acc.add_command(label='Log Out', command=lambda:[logout(),rot.destroy(),v.login()])
        acc.add_command(label='Log Out & Exit', command=lambda:[logout(),rot.destroy()])
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
        #canvas.create_image(0, 0, image=filename, anchor="nw")
        canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
        canvas.create_text(960, 130, text=f"Welcome to your inventory, {o[0]} ", fill="white", font=("courier", 20, "italic"))
        canvas.create_text(75, 20, text=f"Logged-in as {o[0]}", fill="white", font=("courier", 10, "italic"))
        srch=t.StringVar()
        piid=t.StringVar()
        pnnm=t.StringVar()
        pqqt=t.StringVar()
        pddc=t.StringVar()
        prrc=t.StringVar()
        emma=t.StringVar()

        canvas.create_text(205, 230, text="Search Inventory by product name:", fill="turquoise",font=("courier", 15, "italic"))
        canvas.create_text(110, 490, text="Product ID:", fill="turquoise",font=("courier", 15, "italic"))
        pid = t.Entry(rot, relief='groove', bg='light blue',textvariable=piid, font=('courier', 15, 'normal'))
        canvas.create_window(349, 490, window=pid)
        canvas.create_text(110, 540, text="Product Name:", fill="turquoise", font=("courier", 15, "italic"))
        pnm = t.Entry(rot, relief='groove', bg='light blue',textvariable=pnnm, font=('courier', 15, 'normal'))
        canvas.create_window(349, 540, window=pnm)
        canvas.create_text(110, 590, text="Product Qty.:", fill="turquoise", font=("courier", 15, "italic"))
        pqt = t.Entry(rot, relief='groove', bg='light blue',textvariable=pqqt, font=('courier', 15, 'normal'))
        canvas.create_window(349, 590, window=pqt)
        canvas.create_text(110, 640, text="Product Dsc.:", fill="turquoise", font=("courier", 15, "italic"))
        pdc = t.Entry(rot, relief='groove', bg='light blue',textvariable=pddc, font=('courier', 15, 'normal'))
        canvas.create_window(349, 640, window=pdc)
        canvas.create_text(114, 690, text="Product price:", fill="turquoise", font=("courier", 15, "italic"))
        prc = t.Entry(rot, relief='groove', bg='light blue',textvariable=prrc, font=('courier', 15, 'normal'))
        canvas.create_window(349, 690, window=prc)
        canvas.create_text(114, 740, text="emi available:", fill="turquoise", font=("courier", 15, "italic"))
        ema = t.Entry(rot, relief='groove', bg='light blue',textvariable=emma, font=('courier', 15, 'normal'))
        canvas.create_window(349, 740, window=ema)
        adp = t.Button(rot, width=33, height=1, bg="turquoise", text='Add Product', command=lambda: [add_prod()])
        canvas.create_window(349, 790, window=adp)
        udp = t.Button(rot, width=33, height=1, bg="turquoise", text='Update Product', command=lambda: [selection()])
        canvas.create_window(349, 840, window=udp)
        dp = t.Button(rot, width=33, height=1, bg="turquoise", text='Reset Fields', command=lambda: [res()])
        canvas.create_window(349, 890, window=dp)
        rp = t.Button(rot, width=33, height=1, bg="turquoise", text='Delete Product', command=lambda: [deltprod()])
        canvas.create_window(349, 940, window=rp)

        canvas.create_text(355, 400, text="-Select a row from the data and click on 'Update Product' \nto edit/delete it. \n-Enter New Product Details in the boxes, \n and click on 'Add Product' to add it to the inventory. ", fill="turquoise",font=("courier", 15, "italic"))
        ent = t.Entry(rot, relief='groove', bg='light blue',textvariable=srch, font=('courier', 15, 'normal'))
        canvas.create_window(530, 230, window=ent)
        sr=t.Button(rot, width=33, height=1, bg="turquoise", text='Search',command=lambda: [search()])
        canvas.create_window(530,280,window=sr)
        rset=t.Button(rot, width=33, height=1, bg="turquoise", text='Reset',command=lambda: [rst()])
        canvas.create_window(530,330,window=rset)



        style = ttk.Style(rot)
        style.theme_use("clam")
        style.configure("Treeview", background="black", fieldbackground="black", foreground="turquoise")
        columns = ('pid', 'p_name', 'p_qty', 'p_dsc', 'p_prc', 'emi')
        tree = ttk.Treeview(rot, columns=columns, show='headings',height=39)
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
        pric = []
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
            pric.append(uip)
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
        for i in range(0, k):
            tree.insert('', t.END, values=(id[i], nm[i], qt[i], ds[i], pric[i], emi[i]))
        canvas.create_window(1301, 580, window=tree)
        scrollbar = ttk.Scrollbar(rot, orient=t.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        canvas.create_window(1910, 300, window=scrollbar)
        def rst():
            ent.delete(0, t.END)
            fetchdata = tree.get_children()
            for f in fetchdata:
                tree.delete(f)
            for i in range(0, k):
                tree.insert('', t.END, values=(id[i], nm[i], qt[i], ds[i], pric[i], emi[i]))
        def search():
            tree.selection()
            fetchdata = tree.get_children()
            for f in fetchdata:
                tree.delete(f)
            name = srch.get()
            c.execute("select product_id, product_name,product_qty, product_description, product_price, emi_available from items where product_name = '"+name+"' ")
            data = c.fetchall()
            for d in data:
                tree.insert("", t.END, values=d)
            if (len(name) < 2) or (not name.isalpha()):
                messagebox.showerror("fail", "invalid name")
                rst()


        def add_prod():
            piiid=piid.get()
            pnnnm=pnnm.get()
            pqqqt=pqqt.get()
            pdddc=pddc.get()
            prrrc=prrc.get()
            emmma=emma.get()
            if piiid==id[k-1]:
                messagebox.showerror("Repeating ID", "Enter Unique Product ID")
            elif str(piiid)=="" or str(pnnnm)=="" or str(pqqqt)=="" or str(pdddc)=="" or str(prrrc)=="" or str(emmma)=="":
                messagebox.showerror("Empty Fields", "Make sure None of the fields are empty.")
            else:
                try:
                    fo = open("usr.txt", "r+")
                    of = fo.readlines()
                    tree.insert('', t.END, values=(piiid,pnnnm,pqqqt,pdddc,prrrc,emmma))
                    c.execute("insert into items values('"+piiid+"','"+pnnnm+"','"+pqqqt+"','"+pdddc+"','"+of[0]+"','"+prrrc+"','"+emmma+"')")
                except:
                    messagebox.showerror("Error","Something went wrong, please try again.")
        def res():
            pid.delete(0, t.END)
            pnm.delete(0, t.END)
            pqt.delete(0, t.END)
            pdc.delete(0, t.END)
            prc.delete(0, t.END)
            ema.delete(0, t.END)


        def selection():
            res()
            curItem = tree.focus()
            w = tree.item(curItem)['values']
            pid.insert(0, w[0])
            pnm.insert(0, w[1])
            pqt.insert(0, w[2])
            pdc.insert(0, w[3])
            prc.insert(0, w[4])
            ema.insert(0, w[5])
        def deltprod():
            curItem = tree.focus()
            w = tree.item(curItem)['values']
            tree.delete(curItem)
            u = str(w[0])
            c.execute("delete from items where product_id='" + u + "'")
            res()






        opt = t.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=opt)
        opt.add_command(label='Add Product', command=lambda: [add_prod()])
        opt.add_command(label='Delete Product', command=lambda: [deltprod()])
        opt.add_command(label='Update Product', command=lambda: [selection()])
        rot.config(menu=menubar)

        rot.mainloop()


    btn = t.Button(root, width=40, height=1, bg="turquoise",font=("courier", 20, "bold"), text='Open Inventory', command=lambda: [root.destroy(),inventory()])
    canvas.create_window(1490,600,window=btn)
    btn = t.Button(root, width=40, height=1, bg="turquoise", font=("verdana", 10), text='Approve & Dispatch Order', command=lambda: [appr(),deletefrmtree()])
    canvas.create_window(1490, 740, window=btn)
    btn = t.Button(root, width=40, height=1, bg="turquoise", font=("verdana", 10), text='Reject Order',command=lambda: [rej(),deletefrmtree()])
    canvas.create_window(1490, 830, window=btn)
    btn = t.Button(root, width=40, height=1, bg="turquoise", font=("verdana", 10), text='Exit',command=lambda: [root.destroy()])
    canvas.create_window(1490, 920, window=btn)

    inv=t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Inventory', menu=inv)
    inv.add_command(label='View inventory', command=lambda:[root.destroy(), inventory()])
    root.config(menu=menubar)
    c.execute("select product_name from items where vendor_id='"+o[0]+"'")
    ty = []
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ty.append(uip)
    c.execute("select product_qty from items where vendor_id='"+o[0]+"'")
    y = []
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        y.append(int(uip))

    c.execute("select total_value from orders where vendor_id='" + o[0] + "'")
    yi = []
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        yi.append(int(uip))

    c.execute("select order_quantity from orders where vendor_id='" + o[0] + "'")
    iy = []
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        iy.append(int(uip))



    data2 = {'Value': yi, 'Quantity': iy}
    df2 = DataFrame(data2, columns=['Value'])
    df3 = DataFrame(data2, columns=['Quantity'])
    figure2 = plt.Figure(figsize=(5, 4), dpi=100,facecolor="turquoise")
    ax2 = figure2.add_subplot(111)
    ax2.set_facecolor("black")
    line2 = FigureCanvasTkAgg(figure2, root)
    lo = line2.get_tk_widget()
    df2 = df2[['Value']]
    df3 = df3[['Quantity']]
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    df3.plot(kind='line', legend=True, ax=ax2, color='b', marker='o', fontsize=10)
    ax2.set_title('Value and quantity for most recent orders')
    ax2.set_xlabel('Quantity')
    ax2.set_ylabel('Price')


    figure1 = Figure(figsize=(4, 3), dpi=100, facecolor="turquoise")
    subplot1 = figure1.add_subplot(111)
    subplot1.set_facecolor("black")
    subplot1.bar(ty, y, color='lightblue')
    subplot1.set_title("Quantity per Product")
    bar1 = FigureCanvasTkAgg(figure1, root)
    bart = bar1.get_tk_widget()


    figure2 = Figure(figsize=(4, 3), dpi=100,facecolor="turquoise")
    subplot2 = figure2.add_subplot(111)
    subplot2.set_facecolor("black")
    subplot2.pie(y, labels=ty, autopct='%1.1f%%', shadow=True, startangle=90)
    subplot2.axis('equal')
    subplot2.set_title("Inventory Product Share")
    pie2 = FigureCanvasTkAgg(figure2, root)
    bar=pie2.get_tk_widget()



    figure3 = plt.Figure(figsize=(5, 4), dpi=100,facecolor="turquoise")
    ax3 = figure3.add_subplot(111)
    ax3.set_facecolor("white")
    ax3.scatter(y, ty, color='b')
    scatter3 = FigureCanvasTkAgg(figure3, root)
    sc=scatter3.get_tk_widget()
    ax3.legend(['Product Price'])
    ax3.set_xlabel('Price')
    ax3.set_ylabel('Product')
    ax3.set_title('Statistics for Product v/s Price')

    canvas.create_window(280, 430, window=sc)
    canvas.create_window(790, 430, window=lo)
    canvas.create_window(1270, 383, window=bart)
    canvas.create_window(1690, 383, window=bar)
    canvas.create_window(1240, 740, window=scrollbar)
    canvas.create_window(630, 830, window=tree)
    root.mainloop()
def customerhome():
    f = open("usr.txt", "r+")
    o = f.readlines()
    rot = t.Tk()
    rot.title(f'MANAGER+ | E-Shop | Client - {o[0]}')
    rot.geometry('1920x1080')
    canvas = t.Canvas(rot, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)
    def logout():
        f1 = open("usr.txt", "w")
        f1.close()
        f2 = open("crclstp.txt", "w")
        f2.write('ctagakjdkasdnal')
        f2.close()
        rot.destroy()
        v.login()
    menubar = t.Menu(rot)
    nav = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Navigation', menu=nav)
    nav.add_command(label='Your Orders', command=lambda: [rot.destroy(),showorders()])
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
    canvas.create_text(960, 130, text=f"Welcome to our E-Shop, {o[0]} ", fill="white",
                       font=("courier", 20, "italic"))
    canvas.create_text(75, 20, text=f"Logged-in as {o[0]}", fill="white", font=("courier", 10, "italic"))
    srch = t.StringVar()
    piid = t.StringVar()
    pnnm = t.StringVar()
    pqqt = t.StringVar()
    pddc = t.StringVar()
    prrc = t.StringVar()
    emma = t.StringVar()

    canvas.create_text(205, 230, text="Search Shop by product name:", fill="turquoise",
                       font=("courier", 15, "italic"))
    canvas.create_text(110, 490, text="Product ID:", fill="turquoise", font=("courier", 15, "italic"))
    pid = t.Entry(rot, relief='groove', bg='light blue', textvariable=piid, font=('courier', 15, 'normal'))
    canvas.create_window(349, 490, window=pid)
    canvas.create_text(110, 540, text="Product Name:", fill="turquoise", font=("courier", 15, "italic"))
    pnm = t.Entry(rot, relief='groove', bg='light blue', textvariable=pnnm, font=('courier', 15, 'normal'))
    canvas.create_window(349, 540, window=pnm)
    canvas.create_text(110, 590, text="Product Qty.:", fill="turquoise", font=("courier", 15, "italic"))
    pqt = t.Entry(rot, relief='groove', bg='light blue', textvariable=pqqt, font=('courier', 15, 'normal'))
    canvas.create_window(349, 590, window=pqt)
    canvas.create_text(110, 640, text="Product Dsc.:", fill="turquoise", font=("courier", 15, "italic"))
    pdc = t.Entry(rot, relief='groove', bg='light blue', textvariable=pddc, font=('courier', 15, 'normal'))
    canvas.create_window(349, 640, window=pdc)
    prc = t.Entry(rot, relief='groove', bg='light blue', textvariable=prrc, font=('courier', 15, 'normal'))
    ema = t.Entry(rot, relief='groove', bg='light blue', textvariable=emma, font=('courier', 15, 'normal'))
    adp = t.Button(rot, width=33, height=1, bg="turquoise", text='Place Order', command=lambda: [add_prod()])
    canvas.create_window(349, 690, window=adp)
    udp = t.Button(rot, width=33, height=1, bg="turquoise", text='Select Item', command=lambda: [selection()])
    canvas.create_window(349, 740, window=udp)
    dp = t.Button(rot, width=33, height=1, bg="turquoise", text='Reset Fields', command=lambda: [res()])
    canvas.create_window(349, 790, window=dp)

    canvas.create_text(355, 400,
                       text="-Select a row from the data and click on 'Select Item' \nto edit your order. \n-Enter New Order Details in the boxes, \n and click on ' Place Order' to Confirm your order. ",
                       fill="turquoise", font=("courier", 15, "italic"))
    ent = t.Entry(rot, relief='groove', bg='light blue', textvariable=srch, font=('courier', 15, 'normal'))
    canvas.create_window(530, 230, window=ent)
    sr = t.Button(rot, width=33, height=1, bg="turquoise", text='Search', command=lambda: [search()])
    canvas.create_window(530, 280, window=sr)
    rset = t.Button(rot, width=33, height=1, bg="turquoise", text='Reset', command=lambda: [rst()])
    canvas.create_window(530, 330, window=rset)

    style = ttk.Style(rot)
    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="black", foreground="turquoise")
    columns = ('pid', 'p_name', 'p_qty', 'p_dsc', 'p_prc', 'emi')
    tree = ttk.Treeview(rot, columns=columns, show='headings', height=39)
    tree.heading('pid', text='product id')
    tree.heading('p_name', text='product name')
    tree.heading('p_qty', text='product qty')
    tree.heading('p_dsc', text='product desc')
    tree.heading('p_prc', text='product price')
    tree.heading('emi', text='EMI available')
    s = []
    id = []
    nm = []
    qt = []
    ds = []
    pric = []
    emi = []

    c.execute("select product_id from items")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        id.append(uip)
    c.execute("select product_qty from items")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        qt.append(uip)
    c.execute("select product_name from items")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        nm.append(uip)
    c.execute("select product_description from items")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ds.append(uip)
    c.execute("select product_price from items")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        pric.append(uip)
    c.execute("select emi_available from items")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        emi.append(uip)
    c.execute("select product_id from items")
    k = 0
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
        ui = int(uip)
        s.append(ui)
    for i in s:
        k += 1
    for i in range(0, k):
        tree.insert('', t.END, values=(id[i], nm[i], qt[i], ds[i], pric[i], emi[i]))

    scrollbar = ttk.Scrollbar(rot, orient=t.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    canvas.create_window(1301, 580, window=tree)
    canvas.create_window(1910, 300, window=scrollbar)

    def rst():
        fetchdata = tree.get_children()
        for f in fetchdata:
            tree.delete(f)
        for i in range(0, k):
            tree.insert('', t.END, values=(id[i], nm[i], qt[i], ds[i], pric[i], emi[i]))

    def search():
        tree.selection()
        fetchdata = tree.get_children()
        for f in fetchdata:
            tree.delete(f)
        name = srch.get()
        c.execute(
            "select product_id, product_name,product_qty, product_description, product_price, emi_available from items where product_name = '" + name + "' ")
        data = c.fetchall()
        for d in data:
            tree.insert("", t.END, values=d)
        if (len(name) < 2) or (not name.isalpha()):
            messagebox.showerror("fail", "invalid name")
            rst()

    def add_prod():
        piiid = piid.get()
        pnnnm = pnnm.get()
        pqqqt = pqqt.get()
        pdddc = pddc.get()
        c.execute("select product_price from items where product_id='"+piiid+"'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')

        ttl=int(pqqqt)*float(uip)
        c.execute("select vendor_id from items where product_id='" + piiid + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uil = kik.strip(',').replace('\'', '')
        rwdpt=int(pqqqt)
        if str(piiid) == "" or str(pnnnm) == "" or str(pqqqt) == "" or str(pdddc) == "":
            messagebox.showerror("Empty Fields", "Make sure None of the fields are empty.")
        else:
            try:
                fo = open("usr.txt", "r+")
                of = fo.readlines()
                c.execute("insert into orders values('" + piiid + "','" + pnnnm + "','" + str(ttl) + "','" + uil + "','" + of[0] + "','"+pqqqt+"','"+str(rwdpt)+"')")
                messagebox.showinfo("Success","Your Order has been placed successfully")
            except:
                messagebox.showerror("Error", "Something went wrong, please try again.")


    def res():
        pid.delete(0, t.END)
        pnm.delete(0, t.END)
        pqt.delete(0, t.END)
        pdc.delete(0, t.END)
        prc.delete(0, t.END)
        ema.delete(0, t.END)

    def selection():
        res()
        curItem = tree.focus()
        w = tree.item(curItem)['values']
        pid.insert(0, w[0])
        pnm.insert(0, w[1])
        pqt.insert(0, w[2])
        pdc.insert(0, w[3])
        prc.insert(0, w[4])
        ema.insert(0, w[5])

    def deltprod():
        curItem = tree.focus()
        w = tree.item(curItem)['values']
        tree.delete(curItem)
        u = str(w[0])
        c.execute("delete from items where product_id='" + u + "'")
        res()


    def showorders():

        f = open("usr.txt", "r+")
        o = f.readlines()
        rt = t.Tk()
        rt.title(f'MANAGER+ | Orders | Client - {o[0]}')
        rt.geometry('1920x1080')
        canvas = t.Canvas(rt, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)

        def logout():
            f1 = open("usr.txt", "w")
            f1.close()
            f2 = open("crclstp.txt", "w")
            f2.write('ctagakjdkasdnal')
            f2.close()
            rot.destroy()
            v.login()

        menubar = t.Menu(rt)
        nav = t.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Navigation', menu=nav)
        nav.add_command(label='Back to E-Shop', command=lambda: [rt.destroy(),customerhome()])
        nav.add_separator()
        nav.add_command(label='Exit', command=lambda: [rt.destroy()])

        acc = t.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Account', menu=acc)
        acc.add_command(label='Log Out', command=logout)
        acc.add_command(label='Log Out & Exit', command=lambda: [logout(), rt.destroy()])
        acc.add_separator()
        acc.add_command(label='Exit', command=rt.destroy)

        def time():
            string = strftime('%A, %b %d, %H:%M:%S %p, %Y')
            labl.config(text=string)
            labl.after(1000, time)

        labl = t.Label(rt, font=('calibri', 15), bg='black', foreground='white')
        labl.pack()
        time()
        canvas.create_window(960, 95, window=labl)
      #  filename = t.PhotoImage(file="C:\\Users\dh1011tu\Downloads\wallpaperflare.com_wallpaper (4) (1).png")
      #  canvas.create_image(0, 0, image=filename, anchor="nw")
        canvas.create_text(960, 50, text="MANAGER+", fill="turquoise", font=("courier", 50, "italic"))
        canvas.create_text(960, 130, text=f"Orders Summary for {o[0]} ", fill="white",
                           font=("courier", 20, "italic"))
        canvas.create_text(75, 20, text=f"Logged-in as {o[0]}", fill="white", font=("courier", 10, "italic"))
        srch = t.StringVar()
        piid = t.StringVar()
        pnnm = t.StringVar()
        pqqt = t.StringVar()
        pddc = t.StringVar()
        prrc = t.StringVar()
        emma = t.StringVar()

        canvas.create_text(205, 230, text="Search Orders by product name:", fill="turquoise",
                           font=("courier", 15, "italic"))
        canvas.create_text(355, 400,
                           text="-Select a row from the data and click on 'Cancel Order' \nto Cancel your order.",
                           fill="turquoise", font=("courier", 15, "italic"))
        ent = t.Entry(rt, relief='groove', bg='light blue', textvariable=srch, font=('courier', 15, 'normal'))
        canvas.create_window(530, 230, window=ent)
        sr = t.Button(rt, width=33, height=1, bg="turquoise", text='Search', command=lambda: [search()])
        canvas.create_window(530, 280, window=sr)
        rset = t.Button(rt, width=33, height=1, bg="turquoise", text='Reset', command=lambda: [rst()])
        canvas.create_window(530, 330, window=rset)
        adp = t.Button(rt, width=33, height=1, bg="turquoise", text='Cancel Order', command=lambda: [deltprod()])
        canvas.create_window(349, 490, window=adp)

        style = ttk.Style(rt)
        style.theme_use("clam")
        style.configure("Treeview", background="black", fieldbackground="black", foreground="turquoise")
        columns = ('oid', 'p_name', 't_vlv', 'v_id', 'ord_qty', 'rwd_pt')
        tree = ttk.Treeview(rt, columns=columns, show='headings', height=39)
        tree.heading('oid', text='Order ID')
        tree.heading('p_name', text='Product Name')
        tree.heading('t_vlv', text='Total Value')
        tree.heading('v_id', text='Vendor ID')
        tree.heading('ord_qty', text='Order Quantity')
        tree.heading('rwd_pt', text='Reward Points')
        s = []
        id = []
        nm = []
        qt = []
        ds = []
        prc = []
        emi = []
        c.execute("select order_id from orders where customer_id='" + o[0] + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
            id.append(uip)
        c.execute("select product_name from orders where customer_id='" + o[0] + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
            qt.append(uip)
        c.execute("select total_value from orders where customer_id='" + o[0] + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
            nm.append(uip)
        c.execute("select vendor_id from orders where customer_id='" + o[0] + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
            ds.append(uip)
        c.execute("select order_quantity from orders where customer_id='" + o[0] + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
            prc.append(uip)
        c.execute("select reward_point from orders where customer_id='" + o[0] + "'")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
            emi.append(uip)

        c.execute("select order_id from orders where customer_id='" + o[0] + "'")
        k = 0
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uip = kik.strip(',').replace('\'', '')
            ui = int(uip)
            s.append(ui)
        for i in s:
            k += 1
        for i in range(0, k):
            tree.insert('', t.END, values=(id[i], qt[i], nm[i], ds[i], prc[i], emi[i]))
        scrollbar = ttk.Scrollbar(rt, orient=t.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        canvas.create_window(1301, 580, window=tree)
        canvas.create_window(1910, 300, window=scrollbar)
        def rst():
            fetchdata = tree.get_children()
            for f in fetchdata:
                tree.delete(f)
            for i in range(0, k):
                tree.insert('', t.END, values=(id[i], qt[i], nm[i], ds[i], emi[i], emi[i]))

        def search():
            tree.selection()
            fetchdata = tree.get_children()
            for f in fetchdata:
                tree.delete(f)
            name = srch.get()
            c.execute(
                "select product_id, product_name,product_qty, product_description, product_price, emi_available from items where product_name = '" + name + "' ")
            data = c.fetchall()
            for d in data:
                tree.insert("", t.END, values=d)
            if (len(name) < 2) or (not name.isalpha()):
                messagebox.showerror("fail", "invalid name")
                rst()






        def deltprod():
            curItem = tree.focus()
            w = tree.item(curItem)['values']
            tree.delete(curItem)
            u = str(w[0])
            c.execute("delete from orders where order_id='" + u + "'")
            messagebox.showinfo("Success","This Order has been canceled successfully")

        opt = t.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=opt)
        opt.add_command(label='Place Order', command=lambda: [add_prod()])
        opt.add_command(label='Select Item', command=lambda: [deltprod()])
        opt.add_command(label='Reset Fields', command=lambda: [res()])
        rt.config(menu=menubar)

        rt.mainloop()


    opt = t.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Options', menu=opt)
    opt.add_command(label='Place Order', command=lambda: [add_prod()])
    opt.add_command(label='Select Item', command=lambda: [deltprod()])
    opt.add_command(label='Reset Fields', command=lambda: [res()])
    rot.config(menu=menubar)

    rot.mainloop()
def rolecheck():
    f = open("usr.txt", "r+")
    o = f.readlines()
    c.execute("select role from users where user_id='" + o[0] + "'")
    for i in c:
        kik = (str(i).strip('()').replace('\'', ''))
        uip = kik.strip(',').replace('\'', '')
    if uip == "Vendor":
        vendorhome()
    elif uip == "Client":
        customerhome()

