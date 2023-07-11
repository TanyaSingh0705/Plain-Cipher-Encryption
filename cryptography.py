def Encryption(s,k,n,option):
    encstr=" "
    for i in range (0,n):
        for c in s[i]:
            if(ord(c))>=65 and (ord(c)<=90):
                temp = (ord(c) + k[i])
                if temp>90:
                    temp = temp % 90 + 64
                encstr = encstr + chr(temp)
            elif(ord(c))>=97 and (ord(c)<=122):
                temp = (ord(c) + k[i])
                if temp>122:
                    temp = temp % 122 + 96
                encstr = encstr + chr(temp)
            else:
                encstr = encstr + chr(ord(c)+k[i])
        encstr = encstr + " "
        i = i + 1
        
    if option == 1:
        return encstr
    
    elif option == 2:
        rev = []
        word = []
        encstr = encstr.strip()
        word = encstr.split()
        
        for i in range (0,n):
            revstr = " "
            for c in word[i]:
                revstr = c + revstr
            rev.append(revstr)
            i = i + 1
        en = " ".join(rev)
        return en
    
    else:
        return -1

def Decryption(s,k,n,option):
    p = Encryption(s,k,n,option)
    print("Encrypted message is : " + p)
    decstr = " "
    
    en = []
    en = p.split()
    
    if option == 1:
        for i in range (0,n):
            for c in en[i]:
                if((ord(c))>=65) and ((ord(c))<=90):
                    decstr = decstr + chr((ord(c) - k[i]-65) % 26 + 65)
                elif((ord(c))>=97) and ((ord(c))<=122):
                    decstr = decstr + chr((ord(c) - k[i] - 97) % 26 + 97)
                else:
                    decstr = decstr + chr(ord(c)-k[i])
            decstr = decstr + " "
            i = i +1
        return decstr
    
    elif option == 2:
        for i in range (0,n):
            for c in en[i]:
                if((ord(c))>=65) and ((ord(c))<=90):
                    decstr = decstr + chr((ord(c) - k[i]-65) % 26 + 65)
                elif((ord(c))>=97) and ((ord(c))<=122):
                    decstr = decstr + chr((ord(c) - k[i] - 97) % 26 + 97)
                else:
                    decstr = decstr + chr(ord(c)-k[i])
            decstr = decstr + " "
            i = i +1
        rev = []
        word = []
        decstr = decstr.strip()
        word = decstr.split()
        
        for i in range (0,n):
            revstr = " "
            for c in word[i]:
                revstr = c + revstr
            rev.append(revstr)
            i = i + 1
        dec = " ".join(rev)
        
        return dec

    else:
        return -1

message = input("Enter the plain text : ")

word = []
word = message.split()
n = len(word)
key = []

for i in range (0,n):
    count = 0
    for char in word[i] :
        count = count + 1
    count = count % 26 + 1
    key.append(count)
    i = i+1
    
print(key)

print("\nEnter 1.Security \t 2.High Security\n")
op = int(input("Enter Choice : "))

print("Enter 1.Encryprion \t 2.Decryption \n")
ch = int(input("Enter choice : "))

if ch == 1:
    en = Encryption(word,key,n,op)
    print("Encrypted Data : "+ en)
elif ch == 2:
    de = Decryption(word,key,n,op)
    print("Decrypted Data : "+ de)
else:
    print("Enter Valid Choice .")
