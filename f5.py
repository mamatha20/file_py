f=open("mamatha.txt","r")
count=0
txt=f.read()
s=txt.split()
for i in s:
    if i=="mamatha":
        count+=1
    print("total occurence=",count)
f.close()

     