import os
import random
import smtplib
import sqlite3 as s
import urllib.request
import bs4
import xlsxwriter
a=s.connect("vicky1.db")
a.execute('create table if not exists bank1(id int(10),name varchar(50),accountno varchar(20),password varchar(20),mail varchar(50) unique)')
re=' '
mail=' '
pas=' '
yr=xlsxwriter.Workbook("bank1.xlsx")
def excel(sor,ye):
    
    sor=sor[0:5]
    wor=[]
    cou=[]
    print(ye)
    for z in range(5):
        wor.append(sor[z][0])
        cou.append(sor[z][1])
    y=yr.add_worksheet(ye)
    y.write(0,0,"words")
    y.write(0,1,"count")
    row=1
    col=0
    for b in range(5):
        y.write(row,col,wor[b])
        y.write(row,col+1,cou[b])
        row+=1
    chart=yr.add_chart({"type":"column"})
    chart.add_series({"categories":"="+ye+"!A2:A6","values":"="+ye+"!B2:B6"})
    y.insert_chart("D2",chart)
    

def create():
    user=input("Name:")
    mail=input("Mailid:")
    b=a.execute('select count(*) from bank1')
    for c in b:
        print(c)
    e=c[0]+1
    r='000000'+str(e)
    re='655528'+r[-5:]
    print("AccountNo:"+re)
    ch=[x for x in range(10)]
    y=[chr(x) for x in range(ord('A'),ord('z'))]
    ye=[chr(x)for x in range(ord('A'),ord('z'))]
    z=['+','-','/','*','@','!']
    pas=''
    for i in range(2):
        p=random.choice(ch)
        pas+=str(p)
        p=random.choice(y)
        pas+=str(p)
        p=random.choice(ye)
        pas+=str(p)
        p=random.choice(z)
        pas+=str(p)
    print("Password:"+pas)
    a.execute('insert into bank1 values(?,?,?,?,?)',(e,user,re,pas,mail))
    a.commit()
    b=a.execute('select * from bank1')
    for c in b:
        print(c)
    msg="Account no"+str(re)+" "+"Password"+str(pas)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vigneshwariarumugam64@gmail.com','deebigaa27')
    server.sendmail("vigneshwariarumugam64@gmail.com",mail,msg)
    print("sent")
def login():
    user=input("account no/email")
    pas=input("password")
    b=a.execute("select * from bank1 where accountno=? or mail=? and password=?",(re,mail,pas))
    c=' '
    for c in b:
        print(str(c))
    if c!=0:
        print("success")
        url()
    else:
        print("failure")
        
def forget():
    ac=input("accountno")
    b=a.execute("select * from bank1 where accountno=?",([ac]))
    for c in  b:
        print(c[3])
def main():
    b=a.execute("select * from bank1")
    for c in b:
        print(c)
    ye=input("1.create 2.login 3.forgetpassword")
    if ye.lower()=="create" or ye=="1":
        create()
    elif ye.lower()=="login" or ye=="2":
        login()
    elif ye.lower()=="forget" or ye=="3":
        forget()
def url():
    x=input("url")
    ye="http://"+x
    y=urllib.request.urlopen(ye)
    k=bs4.BeautifulSoup(y,"html.parser")
    for c in k(["style","script"]):
        c.extract()
    y=k.get_text()
    y=y.split("\n")
    y=''.join(y)
    y=y.split(" ")
    dic={}
    yk=open("un.txt","r").read().split(" ")
    for c in y:
        if c not in yk:
            dic[c]=y.count(c)
    sor=sorted(dic.items(),key=lambda t:t[1],reverse=True)
    print(sor[0:5])
    excel(sor,x)
    yr.close()
    os.system(' start bank1.xlsx ')
    

while 1:
    try:
        main()
    except Exception as e:
            print(e)
    z=input("do you wish to continue:")
    if z=="yes":
        continue
    else:
        break


sss
