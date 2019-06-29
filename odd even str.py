# odd-even-str
s=input()
h=[]
l=[]
for i in range (len(s)):
    f=i%2
    if f==0:
        h.insert(i,s[i])
    else:
        l.insert(i,s[i])
print(''.join(map(str,h)),end=' ')
print(''.join(map(str,l)),end=' ')
    
    

