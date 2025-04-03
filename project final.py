import pickle
import csv
print("_____________________________________________________________________________________________")
print()
print("                                                             TRAIN TICKET BOOKING                                                                                ")
print()
print("_____________________________________________________________________________________________")
print()
print("DO U WANT TO LOG IN OR REGISTER")
print("LOG IN -1")
print("REGISTER-2")
print()
inter=''
b=input("ENTER OPTION")
if b=='2':
    dada='y'
    while dada=='y':
        user=input("enter a new user name :")
        print()
        print("Password must contain * # & @")
        passd=input("enter a password :")
        print("security question")
        sec=input("favorite colour :")
        f=open("passdata.dat","wb+")
        temp=[]
        try:
                while True:
                    b=pickle.load(f)
                    temp.append(b[0])
        except:
                print()
        if user not in temp:
            pickle.dump([user,passd,sec],f)
            temp.append(user)
            f.close()
            dada='n'
        elif user in temp:
            print("--user id already exist--")
            dada='y'
        b=input("TO LOG IN ENTER 1 =")    
if b=='1':
    ans='y'
    while ans=='y':
            user=input("\t\t\t\tENTER USERNAME :")
            passd=input("\t\t\t\tENTER PASSWORD :")
        
            details,temp=[],[]
        
            
            f=open("passdata.dat","rb+")
            f.seek(0)
            try:
                while True:
                    b=pickle.load(f)
                    details.append(b)
                    temp.append(b[0])
                    
            except:
                print()
            
            mom=''
            if user in temp:
                for i in range(0,len(details)):
                    if  [user,passd]==[details[i][0],details[i][1]] :
                            ans='n'
                            mom='y'
                            inter='open'
            else:
                print("\t\t\t\tINVALID USER ID\n\n\n\n\n")
                ans='y'
                mom='n'
                        
                    
                     
            if mom=='':
                print("INCORRECT PASSWORD OR USER-ID")
                ab=input("FORGOT PASSWORD YES / NO :")
                if ab.lower()=='yes':
                    sec=input("Favorite colour")
                    ggo='y'
                    bingo='y'
                    while ggo=='y':
                        for i in range(0,len(details)):
                                if [user,sec]==[details[i][0],details[i][2]]:
                                    passd=input("enter new password")
                                    print("Password must contain * # & @")
                                    print()
                                    bob=input("re-enter password")
                                    if bob==passd:
                                        details[i][1]=passd
                                        f=open("passdata.dat","wb")
                                        for i in details:
                                            pickle.dump(i,f)
                                        f.close()
                                        print()
                                        print("password changed successfully")
                                        ggo='n'
                                    
                                    elif bob!=passd:
                                        print("NOT MATCHING")
                                        bob=input("re-enter password")
                                        if bob==passd:
                                            details[i][1]=passd
                                            f=open("passdata.dat","wb")
                                            for i in details:
                                                pickle .dump(i,f)
                                            f.close()
                                            print()
                                            print("password changed successfully")
                                    bingo='n'
                                ggo='n'
                                            
                                           
                                         
                        if bingo=='y':
                            print("incorrect input")
                            sec=input("Favorite colour")
                            ggo='y'
                    ggo='n'
                    ans='y'

                      
                    
    
if inter=="open":
    print("\tWELCOME",user,"\n")
    print("DO U WANT TO  :              ")
    print("\t BOOK TICKET                  \t1")
    print("\tPREVIOUS BOOKINGS   \t2\n")
    an=input("ENTER OPTION:")
    if an=='1':                        
        lst = [["TIME"+"            "+'TRAIN',"PNR NO."],['KERALA EXPRESS' ,'16345'+"        "+"16:00-2:00"],['AMRITA EXPRESS','20201'+"         "+"20:00-23:51"]]
        bb=['16345','20201']
        for i in lst:
            print(i[1],i[0],sep='\t')
        v,k,J='t','t',[]
        
        while v=='t':
            book=input("enter PNR no.")
            train=input("train name")
            if  book in bb:
                how=int(input("how many persons"))
                for i in range(0,how):
                    print()
                    name=input("\t\t\t\tenter name ")
                    age=input("\t\t\t\tenter age ")
                    gender=input("\t\t\t\tenter gender M/F ")
                    J.append([user,book,train,name,age,gender])
                v='n'
            else:
                print("INVALID PNR NO.")
                V='t'
            f=open("uu.csv","w+",newline="")
            wobj=csv.writer(f)
            for i in range(0,len(J)):
                wobj.writerow(J[i])
            
            f.close()
            import random
            F=open("ticket.csv","w",newline='')
            wobj=csv.writer(F)
            bT, cT=J[0][2],str(J[0][1])
            wobj.writerow([])
            wobj.writerow(["                               "+"_____________________________________________________________________________________________"])
            wobj.writerow([" "])
            wobj.writerow(["                               "+"                                          INDIAN RAILWAYS                               "])
            wobj.writerow(["                               "+"_____________________________________________________________________________________________"])
            wobj.writerow(["                               "+"TRAIN NAME :"+bT.upper()+"        "+"TRAIN NO :"+cT])
            for i in range(0,len(J)):
                jj,Q,W=J[i][3],J[i][4],J[i][5]
                wobj.writerow(["                               "+"NAME - "+jj.upper()+"                 "+'AGE - '+Q+"                 "+'GENDER - '+W.upper()])
                wobj.writerow(["                               "+"BERTH - "+str(random.randint(1,100))+"                 "+"COACH NO -"+"S"+str(random.randint(1,10))])
                wobj.writerow(["                               "+'_____________________________________________________________________________________________'])
            wobj.writerow(["                               "+'_____________________________________________________________________________________________'])
            
            
            F.close()
            print("\t\t\t\t\t\tTICKET BOOKED")
            now=input("to know how to view ticket enter Y")
            if now.lower()=='y':
                print("CLICK ON FILE")
                print("THEN OPEN")
                print("SEARCH FOR ticket.csv")
                print("OPEN THE FILE WITH NOTEPAD")
                
if an=='2':
    f=open("uu.csv","r")
    robj=csv.reader(f)
    j,pk=[],[]
    print("\t\t\PREVIOUS BOOKINGS")
    print()
    print("PNR"+"                "+"TRAIN"+"                 "+"STATUS")
    try:
        for i in robj:
            j.append(i)
            pk.append(i[1])
            
            print(i[1]+"                     "+i[2]+"                     "+"CONFIRMED")
    except:
        print()
    f.close()
   
    
    GO=input("ENTER THE PNR NO. TO DOWNLOAD TICKET :")
    if  GO in pk:
        for i in j:
            if GO in i:
                import random
                f=open("ticket.csv","w")
                wobj=csv.writer(f)
                bT, cT=i[2],str(i[1])
                wobj.writerow([])
                wobj.writerow(["                               "+"_____________________________________________________________________________________________"])
                wobj.writerow([" "])
                wobj.writerow(["                               "+"                                          INDIAN RAILWAYS                               "])
                wobj.writerow(["                               "+"_____________________________________________________________________________________________"])
                wobj.writerow(["                               "+"TRAIN NAME :"+bT.upper()+"        "+"TRAIN NO :"+cT])
                jj,Q,W=i[3],i[4],i[5]
                wobj.writerow(["                               "+"NAME - "+jj.upper()+"                 "+'AGE - '+Q+"                 "+'GENDER - '+W.upper()])
                wobj.writerow(["                               "+"BERTH - "+str(random.randint(1,100))+"                 "+"COACH NO -"+"S"+str(random.randint(1,10))])
                wobj.writerow(["                               "+'_____________________________________________________________________________________________'])
                wobj.writerow(["                               "+'_____________________________________________________________________________________________'])
                f.close()
                
                now=input("to know how to view ticket enter Y")
                if now.lower()=='y':
                    print("CLICK ON FILE")
                    print("THEN OPEN")
                    print("SEARCH FOR ticket.csv")
                    print("OPEN THE FILE WITH NOTEPAD")
                    
        
        
            
    
    
    
