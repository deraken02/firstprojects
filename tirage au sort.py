from random import randint
a=str(input("dilemme? "))
c=int(input("nombre de choix? "))
i=0
while i<c:
    i+=1
    globals()['b'+str(i)]=str(input('choix '+str(i)+'? '))
e=str(input("équité des chances? y/n "))
if e=="y":
    a=randint(1,c)
    d=globals()['b'+str(a)]
    print(d)
i=0
y=0
if e=="n":
    b=randint(1,100)
    print(b)
    while i<c:
        i+=1
        a=int(input('pourcentage choix'+str(i)+' '))
        y+=a
        if a==0 and y<=100:
            print('Erreur pourcentage nul impossible recommence grosse merde')
            print('PS: Je t\'aime')
            i=i-1
        if 1<=b<=y:
             d=globals()['b'+str(i)]
             print (d)
             i=c