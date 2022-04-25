import database
import random
c=database.c
l=['milk','tea','honey','sugar','fork','bowl','stand','cover','bottle', 'apple juice','orange', 'orange juice', 'gumstick', 'pendrive','wallet', 'pen','pen pencil','marker','stamp-pad','notebook','sketchbook','calculator','pencil','mouse','keyboard','battery','powerbank','charger','screen protector','cable','bag','dart board','soft board','cable ties','white board','sanitizer']
o=[100,120,150,180,200,220,250,280,300,320,350,370,400,420,450,490,500,520,550,560,600,630,670,690,700,720,750,790,800,820,840,860,900,930,960,990,1000]
p=[10,30,40,60,75,80,95,100,120,150,180,200,220,250,280,300,320,350,370,400,420,450,490,500]
for i in range(1,10):
    k=random.sample(l,1)[0]
    print(k)
    j=random.sample(o,1)[0]
    print(j)
    f=random.sample(p,1)[0]
    print(f)
    c.execute("insert into items values('"+str(i)+"','"+str(k)+"','"+str(f)+"','"+str(k)+"','ansh','"+str(j)+"','No')")