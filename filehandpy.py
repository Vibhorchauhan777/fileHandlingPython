import os

def countvowels():
    count=0
    f= open("C://Users//vibho//example.txt","r")
    strn= f.read()
    print(strn)
    for x in strn:
        if x =="a" or x =="e" or x =="i" or x =="o" or x =="u" or x =="A" or x =="I" or x == "O" or x =="U" or x =="E":
            count=count+1
    print("The number of vowels int the text file is:", count)
    f.close()


def smallalpha():
    count=0
    f=open("C://Users//vibho//example.txt","r")
    strn= f.read()
    for x in strn:
        if ord(x)>=97 and ord(x)<=122:
            count= count+1
    print("The number of small letters in the file is:", count)
    f.close()

def spaces():
    f= open("C://Users//vibho//example.txt","r")
    strn=f.read()
    count=0
    for x in strn:
        if x == " ":
            count=count+1
    print("The number of spaces in the text file is:", count)
    f.close()

def capitalalpha():
    count=0
    f=open("C://Users//vibho//example.txt","r")
    strn= f.read()
    for x in strn:
        if ord(x)>=65 and ord(x)<=90:
            count= count+1
    print("The number of capital letters in the file is:", count)
    f.close()

def specialchar():
    f= open("C://Users//vibho//example.txt","r")
    strn=f.read()
    count=0
    for x in strn:
        if ord(x)>=33 and ord(x)<=47 or ord(x)>=58 and ord(x)<=64:
            count=count+1
    print("The number of special characters in the text file is:", count)
    f.close()

def digits():
    f= open("C://Users//vibho//example.txt","r")
    strn=f.read()
    count=0
    for x in strn:
        if ord(x)>=48 and ord(x)<=57:
            count=count+1
    print("The number of digits in the text file is:", count)
    f.close()

def encrypter():
    f= open("C://Users//vibho//example.txt","r")
    strn= ' '
    res=' '
    strn=f.read()
    for x in range(0,len(strn)):
        res= res+chr(ord(strn[x])+2)
    print("The encrypted message is",res)
    f.close()


def countqt():
    countq=0
    countt=0
    f= open("C://Users//vibho//example.txt","r")
    strn= f.read()
    for x in strn:
        if x == "t":
            countt=countt+1
        elif x=="q":
            countq=countq+1
    print("The number of  t int the text file is:", countt)
    print("the number of q in the text file is:",countq)
    f.close()

def thisthat():
    countthis=0
    countthat=0
    f= open("C://Users//vibho//example.txt","r")
    L= f.read()
    words= L.split()
    for x in words:
        if x=="this":
            countthis=countthis+1
        elif x=="that":
            countthat=countthat+1
    print("The number of  this int the text file is:", countthis)
    print("the number of that in the text file is:",countthat)
    f.close()

def morethanfive():
    count=0
    f= open("C://Users//vibho//example.txt","r")
    L= f.read()
    words= L.split()
    for x in words:
        if len(x)>5:
            count=count+1
    print("the words having more than 5 letters are:",count)
    f.close()
    

def eitherTorM():
    count=0
    f= open("C://Users//vibho//example.txt","r")
    L= f.read()
    print(L)
    words= L.split()
    for x in words:
        if x[0]=="t" or x[0]=="m" or x[0]=="T"or x[0]=="M":
            count=count+1
    print("The number of words starting with the letter T or M are",count)
    f.close()
    
def endwithT():
    count=0
    f= open("C://Users//vibho//example.txt","r")
    L= f.read()
    print(L)
    words= L.split()
    for x in words:
        for i in x:
            if i[-1]=="t" or i[-1]=="T":
                count=count+1
    print("The number of words having last character as t",count)
    f.close()

#main()
print("Welcome to the Menu Driven program for File Handling:")
print("Select the option:\n 1) count vowels \n 2)count small letters \n 3) count capital letters \n 4)count spaces \n 5)count special characters \n 6)count digits \n 7)encryption \n 8)count this and that \n 9)count words more than 5 \n 10)word startin with either T or M \n 11)word ending with T")
ch= int(input("enter an Option:"))
if ch==1:
    countvowels()
elif ch==2:
    smallalpha()
elif ch==3:
    capitalalpha()
elif ch==4:
    spaces()
elif ch==5:
    specialchar()
elif ch==6:
    digits()
elif ch==7:
    encrypter()
elif ch==8:
    countqt()
elif ch==9:
    thisthat()
elif ch==10:
    morethanfive()
elif ch==11:
    eitherTorM()
elif ch==12:
    endwithT()
    
    
    


